from typing import Any, Callable
import time
import os

class DeviceMonitor:
  def __init__(self,
    address:str,
    ondisconnect:Callable=None,
    onconnect:Callable=None,
    disconnect_threshold=1
    ):

    self.address:str = address
    self.ondisconnect:Callable = ondisconnect
    self.onconnect:Callable = onconnect
    self._connection_state = None
  
    return

  
  def listen(self, refresh_interval=10):
    while True:

      state = self._connected()

      if self._connection_state !=state:
        self._handle_connection_state_change(state)
      
      time.sleep(refresh_interval)
  
  def _connected(self)->bool:
    
    return os.system(f"ping -c 1 {self.address}") == 0
  
  def _handle_connection_state_change(self, state:bool)->Any:
    self._connection_state = state
    if state:
      return self.onconnect()

    return self.ondisconnect()
      