from lan.pinger import Pinger
from hue.client import Client


def main():
    client = Client('192.168.50.16')
    pinger = Pinger(
        '192.168.50.201',
        connected_interval=180,
        disconnected_interval=6,
        on_connect=client.resume,
        on_disconnect=client.stop,
        max_retries=3
    )
    pinger.listen()

if __name__ == "__main__":
    main()