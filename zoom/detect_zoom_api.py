import argparse
import json
from zoomus import ZoomClient

def authenticate_and_query(api_key, api_secret):
    client = ZoomClient(api_key, api_secret)
    # Unfortuantely, this user_id pulls in all meetings when run with
    # admin keys
    user_id='me'
    meetings = client.meeting.list(user_id=user_id, type="upcoming_meetings")
    for meeting in meetings:
        print(meeting)
    users = client.user.list()
    #for user in users:
     #   print(user)
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="O365 Calendar Access")
    parser.add_argument("--zoom-api-key", dest="zoom_api_key", type=str, required=True)
    parser.add_argument("--zoom-api-secret", dest="zoom_api_secret", type=str, required=True)
    args = parser.parse_args()
    authenticate_and_query(args.zoom_api_key, args.zoom_api_secret)
