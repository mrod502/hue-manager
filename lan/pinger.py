from typing import Callable
import time
import os

class Pinger:
    def __init__(
            self,
            address:str,
            connected_interval:int=180,
            disconnected_interval:int=6,
            on_connect:Callable=None,
            on_disconnect:Callable=None,
            max_retries=2
        ):

        self._addr:str = address
        self._connected_interval:int = connected_interval
        self._disconnected_interval:int = disconnected_interval
        self._on_connect:Callable = on_connect
        self._on_disconnect:Callable = on_disconnect
        self._max_retries:int = max_retries
        self._connected:bool = False
        self._retries:int = 0

        return

    def listen(self):
        while True:
            if not self.ping():
                if self._connected:
                    if self._retries < self._max_retries:
                        self._retries += 1
                    else:
                        self._connected = False
                        self._on_disconnect()

            elif not self._connected:
                self._connected = True
                self._retries = 0
                self._on_connect()
                
            self._wait()
    
    def ping(self)->bool:
        return os.system(f"ping -c 1 {self._addr}") == 0

    def _wait(self):
        time.sleep(self._connected_interval if self._connected else self._disconnected_interval)
