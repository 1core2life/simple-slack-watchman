import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', required=True, 
                        help='Slack webhook key')
    parser.add_argument('--cpu', required=True, type=float,
                        help='Limitation for cpu use percentage')
    parser.add_argument('--ram', required=True, type=float,
                        help='Limitation for ram use percentage')
    parser.add_argument('--interval', required=True, type=float,
                        help='Checking loop time')
    parser.add_argument('--url', required=False, type=str,
                        help='check state target url')

    args = parser.parse_args()

    return args