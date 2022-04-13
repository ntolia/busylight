import os
import subprocess
import sys
import time

from zoom.detect_zoom_ps import DetectZoom

class BusylightController:
    def run_once(self):
        dz = DetectZoom()
        zoom_option = '--no-zoom-on'
        if dz.detect():
            zoom_option = '--zoom-on'
        
        dir_path = os.path.dirname(os.path.realpath(__file__))
        docker_cmd = ['/usr/local/bin/docker', 'run', '-e', 'GOVEE_API_KEY', '-e', 'O365_CLIENT_ID',
                '-e', 'O365_SECRET', '--rm',
                '-v', dir_path + ':/usr/src/busylight', 'ntolia/busylight',
                'python', 'busylight.py', zoom_option]
        print(docker_cmd)

        # Run the Docker container
        process = subprocess.Popen(docker_cmd,
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            universal_newlines=True)
        stdout, stderr = process.communicate()
        # print(stdout)
        # print(stderr)

if __name__ == "__main__":
    blc = BusylightController()
    blc.run_once()
