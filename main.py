from phue import Bridge

from hue.client import Client
from lan.device_monitor import DeviceMonitor





def main():

  cli = Client('192.168.50.16')
  m = DeviceMonitor(
    '192.168.50.201',
    ondisconnect=cli.turn_off_the_lights,
    onconnect= lambda: print('hi!'),
    disconnect_threshold=3
  )
  m.listen(120)
  
  pass

if __name__ == "__main__":
  main()