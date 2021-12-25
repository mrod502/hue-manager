from phue import Bridge


class Client(Bridge):

  def __init__(self, bridge_ip:str):
    super().__init__(bridge_ip)
    self.connect()
    print(f"connected to {bridge_ip}")
    print(f"light groups: {self.get_group()}")
  
  def turn_off_the_lights(self):
    for light in self.lights:
      light.on = False
  
  def turn_on_the_lights(self):
    for light in self.lights:
      light.on = True