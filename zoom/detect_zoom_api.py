import argparse
import json
from zoomus import ZoomClient

class DetectZoomAPI:

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def detect(self):
        client = ZoomClient(api_key, api_secret)
        # Unfortuantely, the 'me' user_id pulls in all meetings for all users
        # when run with admin keys. One can list users and then filter out the
        # user one is interested in. However, the JWT token-based also cannot
        # be scoped and so this path was abandonded.
        user_id='me'
        meetings = client.meeting.list(user_id=user_id, type="upcoming_meetings")
        for meeting in meetings:
            print(meeting)
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="O365 Calendar Access")
    parser.add_argument("--zoom-api-key", dest="zoom_api_key", type=str, required=True)
    parser.add_argument("--zoom-api-secret", dest="zoom_api_secret", type=str, required=True)
    args = parser.parse_args()
    dza = DetectZoomAPI(args.zoom_api_key, args.zoom_api_secret)
