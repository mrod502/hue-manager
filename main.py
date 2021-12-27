import sys
from typing import List

from lan.pinger import Pinger
from hue.client import Client


def parse_args()->dict:
    args = {}
    ix = 1
    sys_args:List[str] = sys.argv

    while ix < len(sys_args):
        if sys_args[ix].startswith('--'):
            args[sys_args[ix][2:]] = sys_args[ix+1]
            args+=2
        else:
            ix+=1

    
    return args


def main():
    client = Client(sys.argv[1])
    pinger = Pinger(
        sys.argv[2],
        connected_interval=180,
        disconnected_interval=6,
        on_connect=client.resume,
        on_disconnect=client.stop,
        max_retries=3
    )
    pinger.listen()


if __name__ == "__main__":
    main()