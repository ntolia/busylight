.PHONY: buildimage

buildimage: Dockerfile
        docker build -t "ntolia/busylight:latest" .

dev:
	docker run -e GOVEE_API_KEY -e AZURE_BUSYLIGHT_APP_ID -e AZURE_BUSYLIGHT_CLIENT_ID \
		-e AZURE_BUSYLIGHT_SECRET -it --rm -v ${PWD}:/usr/src/busylight ntolia/busylight \
		/bin/bash
