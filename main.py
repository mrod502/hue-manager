from lan.pinger import Pinger
from hue.client import Client
import time
import json

def main():
    client = Client('192.168.50.16')
    pinger = Pinger(
        '192.168.50.201',
        connected_interval=120,
        disconnected_interval=4,
        on_connect=client.resume,
        on_disconnect=client.stop,
        max_retries=3
    )
    pinger.listen()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        with open('/usb/huemgr/crash.log','w') as f:
            f.write(f"{time.time()} {e.with_traceback()}\n")

