.PHONY: buildimage

buildimage: Dockerfile
        docker build -t "ntolia/busylight:latest" .

dev:
	docker run -e GOVEE_API_KEY -it --rm -v ${PWD}:/usr/src/busylight ntolia/busylight /bin/bash
