import sys
import subprocess

class DetectZoom:

    def detect(self):
        proc1 = subprocess.Popen(["ps", "x"], stdout=subprocess.PIPE)
        proc2 = subprocess.Popen(["grep", "-E", "\-key [0-9]{9,10}"], stdin=proc1.stdout, stdout=subprocess.PIPE)
        proc1.stdout.close()

        output = proc2.communicate()[0]
        if output:
            print("Zoom in session", output)
            return True
        else:
            print("Zoom not in session ")
            return False

if __name__ == "__main__":
    dz = DetectZoom()
    print("Zoom running?", dz.detect())
