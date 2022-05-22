# Govee-enabled Busylight

This code was created in a hurry to set up a pair of [Govee Light Bars
(H6056)](https://www.amazon.com/dp/B096WZXKZP) as a busy light
signal. The light turns on if the code detects either a meeting in
progress (O365 calendar support only) or if Zoom is running.

# Prerequisites

## Tools

- Docker
- `make`
- Python3

## API Keys

- A Govee API key
- Microsoft API keys (needs admin approval)

# Running the Busylight Controller

```bash
make buildimage
python controller.py
```

### Xbar on macOS

[xbar](https://xbarapp.com/) is a very convenient way to run the busylight controller
in a loop. There is an example script (`xbar.1m.sh`) provided to illustrate this use.

# Pointers

## The Zoom Hack

So, this code was written for a Mac. Detecting if Zoom was running via
the Zoom API was possible but it required OAuth support to do it right
and there wasn't an existing library that supported that. A cheaper
and far easier method was to simply run `ps` and check if a Zoom
meeting was in progress.

However, this conflicted with the requirement to run as much
(potentially untrusted) code in a container. So, the hack was to first
detect if Zoom was running and then pass that status in to a container
that ran the rest of the code to both check for meetings and to turn
the busy light on or off.

## References

- [Govee API Docs](https://govee-public.s3.amazonaws.com/developer-docs/GoveeAPIReference.pdf)
- [Govee Python SDK - Unofficial](https://github.com/LaggAt/python-govee-api)
- [How to read Microsoft Outlook Calendars - Setup](https://pietrowicz-eric.medium.com/how-to-read-microsoft-outlook-calendars-with-python-bdf257132318)
- [Zoom Meetings API Endpoint](https://marketplace.zoom.us/docs/api-reference/zoom-api/methods#operation/meetings)
