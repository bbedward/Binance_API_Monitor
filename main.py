import argparse

from monitor import Monitor

if __name__ == '__main__':

    parser = argparse.ArgumentParser('')
    parser.add_argument('--frequency', type=int, help='How often to check binance API (seconds)', default=60)
    parser.add_argument('--symbol', type=str, help='Symbol to monitor binance API for', required=True)

    options = parser.parse_args()

    mon = Monitor(options)
    mon.run()
