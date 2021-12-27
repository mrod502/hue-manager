from typing import Dict
from phue import Bridge


class Client(Bridge):
	def __init__(self, bridge_ip:str):
		super().__init__(bridge_ip)
		self.connect()
		self._state:Dict[str, dict] = self._get_state()

	def stop(self):
		self._state = self._get_state()
		for light in self.lights:
			light.on = False

	def resume(self):
		for light_id in self._state:
			self.set_light(int(light_id), "on", self._state[light_id]['on'])

	def _get_state(self)->Dict[int, dict]:
		state_dict = {}
		lights = self.get_light()

		for light in lights:
			state_dict [light] = {
					'on'	: lights[light]['state']['on'],
					'sat'	: lights[light]['state']['sat'],
					'xy'	: lights[light]['state']['xy'],
				}

		return state_dict