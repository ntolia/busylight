import argparse
import os

from o365.cal import DetectMeeting
from govee.govee import GoveeLights

class Busylight:

    def __init__(self, zoom_on, govee_api_key, o365_client_id, o365_secret):
        self.zoom_on = zoom_on
        self.govee_lights = GoveeLights(govee_api_key)
        self.o365_client_id = o365_client_id
        self.o365_secret = o365_secret

    def toogle_busylight(self):
        if self.zoom_on:
            self.govee_lights.turn_light(True)
            print('🔴')
            return
        
        # Let's check for a calendar invite next
        dm = DetectMeeting(self.o365_client_id, self.o365_secret, os.getcwd() + '/o365/o365_token')
        if dm.detect_meeting():
            self.govee_lights.turn_light(True)
            print('🔴')
            return

        self.govee_lights.turn_light(False)
        print('🟢')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Busylight Controller')
    parser.add_argument('--govee-api-key', dest='govee_api_key', type=str,
        default=os.environ.get('GOVEE_API_KEY'))
    parser.add_argument('--zoom-on', action=argparse.BooleanOptionalAction)
    parser.add_argument('--o365-client-id', dest='o365_client_id', type=str,
        default=os.environ.get('O365_CLIENT_ID'))
    parser.add_argument('--o365-secret', dest='o365_secret_id', type=str,
        default=os.environ.get('O365_SECRET'))
    args = parser.parse_args()

    busy_light = Busylight(args.zoom_on, args.govee_api_key, args.o365_client_id,
        args.o365_secret_id)
    busy_light.toogle_busylight()
