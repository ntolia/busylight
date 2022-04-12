import argparse
import datetime
from O365 import Account, MSGraphProtocol, FileSystemTokenBackend

class DetectMeeting:
    def __init__(self, client_id, secret_id):
        self.credentials = (client_id, secret_id)

        protocol = MSGraphProtocol()
        scopes = ['Calendars.Read.Shared', 'basic']
        token_backend = FileSystemTokenBackend(token_path='./o365_token')
        self.account = Account(self.credentials, protocol=protocol, token_backend=token_backend)

    def detect_meeting(self):
        if not (self.account.is_authenticated):
            account.authenticate(scopes=scopes)
            print('Authenticated!')
        else:
            print('Previously autneticated')

        schedule = self.account.schedule()
        calendar = schedule.get_default_calendar()
        # Create query for -8 to +8 hours from
        now = datetime.datetime.now(datetime.timezone.utc)
        start_time = now - datetime.timedelta(hours=8)
        end_time = now + datetime.timedelta(hours=8)
        query = calendar.new_query('start').greater_equal(start_time)
        query.chain('and').on_attribute('end').less_equal(end_time)

        events = calendar.get_events(query=query)

        for event in events:
            # print("Detected calendar event:", event)

            # Push now forward by two minutes so that we can be proactive
            if event.start <= (now + datetime.timedelta(minutes=2)) and event.end >= now:
                print("Currently in", event)
                return True

        return False
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="O365 Calendar Access")
    parser.add_argument("--client-id", dest="client_id", type=str, required=True)
    parser.add_argument("--secret-id", dest="secret_id", type=str, required=True)    
    args = parser.parse_args()

    dm = DetectMeeting(args.client_id, args.secret_id)
    dm.detect_meeting()
