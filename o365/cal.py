import argparse
import datetime
import pytz
from O365 import Account, MSGraphProtocol, FileSystemTokenBackend

class DetectMeeting:
    def __init__(self, client_id, secret, token_path):
        self.credentials = (client_id, secret)

        protocol = MSGraphProtocol()
        scopes = ['Calendars.Read.Shared', 'basic']
        token_backend = FileSystemTokenBackend(token_path)
        self.account = Account(self.credentials, protocol=protocol, token_backend=token_backend)

    def detect_meeting(self):
        if not (self.account.is_authenticated):
            # Note: The keys expire in 24 months or so
            print('O365 requires authentication')
            self.account.authenticate(scopes=scopes)
        else:
            # print('Previously authenticated')
            pass

        schedule = self.account.schedule()
        calendar = schedule.get_default_calendar()
        # Create query for -8 to +8 hours from
        now = datetime.datetime.now(datetime.timezone.utc)
        start_time = now - datetime.timedelta(hours=8)
        end_time = now + datetime.timedelta(hours=8)
        query = calendar.new_query('start').greater_equal(start_time)
        query.chain('and').on_attribute('end').less_equal(end_time)

        events = calendar.get_events(query=query)
        midnight = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

        for event in events:
            # print("Detected calendar event:", event)

            # Skip all-day events
            if midnight.time() == event.start.time():
                if event.end >= event.start + datetime.timedelta(hours=24):
                    continue

            # Push now forward by two minutes so that we can be proactive
            if event.start <= (now + datetime.timedelta(minutes=2)) and event.end >= now:
                return True

        return False
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="O365 Calendar Access")
    parser.add_argument("--client-id", dest="client_id", type=str, required=True)
    parser.add_argument("--secret", dest="secret", type=str, required=True)
    args = parser.parse_args()

    dm = DetectMeeting(args.client_id, args.secret_id, "./o365_token")
    dm.detect_meeting()
