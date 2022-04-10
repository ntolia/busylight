.PHONY: buildimage

buildimage: Dockerfile
        docker build -t "ntolia/busylight:latest" .

dev:
	docker run -it --rm -v ${PWD}:/usr/src/busylight ntolia/busylight /bin/bash
