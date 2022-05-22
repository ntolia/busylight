import argparse
import asyncio
from typing import Dict

from govee_api_laggat import Govee, GoveeAbstractLearningStorage, GoveeLearnedInfo

class GoveeLights:
    def __init__(self, api_key, light_name):
        self.api_key = api_key
        self.light_name = light_name

    async def _turn_light_on_off(self, state):
        govee = await Govee.create(self.api_key, learning_storage=NullLearningStorage())
        devices, err = await govee.get_devices()
        if not devices:
            print('No devices found')
            await govee.close()
            return

        # Leaving this in here in case it is useful later
        # devices = await govee.get_states()

        device = None
        for device in devices:
            if device.device_name == self.light_name:
                break

        if device is None:
            print('No busylight device found')
            await govee.close()
            return

        if state:
            success, err = await govee.turn_on(device)
            success, err = await govee.set_brightness(device, 50)
            success, err = await govee.set_color(device, (100, 0, 0))
        else:
            success, err = await govee.turn_off(device)

        await govee.close()

    def turn_light(self, state):
        loop = asyncio.get_event_loop_policy().get_event_loop()
        try:
            loop.run_until_complete(self._turn_light_on_off(state))
        finally:
            loop.close()

# To get rid of warnings
class NullLearningStorage(GoveeAbstractLearningStorage):
    async def read(self) -> Dict[str, GoveeLearnedInfo]:
        return (
            {}
        )

    async def write(self, learned_info: Dict[str, GoveeLearnedInfo]):
        persist_this_somewhere = learned_info


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Govee Lights Driver")
    parser.add_argument("--api-key", dest="api_key", type=str, required=True)
    parser.add_argument("--light-name", dest="light_name", type=str,
        default="Busylight")
    args = parser.parse_args()

    govee_lights = GoveeLights(args.api_key, args.light_name)
    govee_lights.turn_light(False)
