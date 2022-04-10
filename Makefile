.PHONY: buildimage spelling

buildimage:
        docker build -t "ntolia/busylight:latest" .
