import argparse
import asyncio
from typing import Dict

from govee_api_laggat import Govee, GoveeAbstractLearningStorage, GoveeLearnedInfo

async def turn_light_on(api_key):
    govee = await Govee.create(api_key)
    devices, err = await govee.get_devices()
    if not devices:
        print('No devices found')
        await govee.close()
        return

    devices = await govee.get_states()

    device = None
    for device in devices:
        if device.device_name == 'Busylight':
            print('Busylight found:', device)
            break

    if device is None:
        print('No busylight device found')
        await govee.close()
        return

    # success, err = await govee.turn_off(device)
    success, err = await govee.turn_on(device)
    success, err = await govee.set_color(device, (100, 0, 0))
    # success, err = await govee.set_brightness(device, 100)

    await govee.close()

async def turn_light_off(api_key):
    govee = await Govee.create(api_key)
    devices, err = await govee.get_devices()
    if not devices:
        print('No devices found')
        await govee.close()
        return

    device = None
    for device in devices:
        if device.device_name == 'Busylight':
            print('Busylight found:', device)
            break

    if device is None:
        print('No busylight device found')
        await govee.close()
        return

    success, err = await govee.turn_off(device)

    await govee.close()


# and your are good to go
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="govee_api_laggat examples")
    parser.add_argument("--api-key", dest="api_key", type=str, required=True)
    args = parser.parse_args()

    # going async ...
    loop = asyncio.get_event_loop_policy().get_event_loop()
    try:
        loop.run_until_complete(turn_light_on(args.api_key))
    finally:
        loop.close()
