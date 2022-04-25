.PHONY: buildimage

buildimage: Dockerfile
	docker build -t "ntolia/busylight:latest" .

dev:
	docker run -e GOVEE_API_KEY -e O365_CLIENT_ID -e O365_SECRET -it --rm \
		-v ${PWD}:/usr/src/busylight ntolia/busylight \
		/bin/bash

busylight:
	docker run -e GOVEE_API_KEY -e O365_CLIENT_ID -e O365_SECRET --rm \
		-v ${PWD}:/usr/src/busylight ntolia/busylight \
		python busylight.py --zoom-on
