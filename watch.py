import requests 
import argparse
import psutil
import time
import socket



parser = argparse.ArgumentParser()
parser.add_argument('--key', required=True, 
                    help='slack webhook key')
parser.add_argument('--cpu', required=True, type=float,
                    help='cpu alert max percentage')
parser.add_argument('--ram', required=True, type=float,
                    help='ram alert max percentage')
parser.add_argument('--interval', required=True, type=float,
                    help='check interval')

args = parser.parse_args()

ALERT_CPU_PERCENT = args.cpu
ALERT_RAM_PERCENT = args.ram

def get_system_state():
    cpu = psutil.cpu_percent(interval=0.1)
    mem_used_percent_size = psutil.virtual_memory().percent
    mem_available_size = psutil.virtual_memory().available/1204**3

    return cpu, mem_used_percent_size, mem_available_size


def check_local_state():
    cpu, mem_used_percent_size, mem_available_size = get_system_state()
    print(cpu, mem_used_percent_size, mem_available_size)

    if cpu > ALERT_CPU_PERCENT or mem_available_size > ALERT_RAM_PERCENT:
        return True
    else:
        return False


def check_network_state():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', 80)) == 0


def send_alert():
    cpu, mem_used_percent_size, mem_available_size = get_system_state()

    message = "CPU: {0}% , RAM: {1}%, Available: {2} GB".format(round(cpu, 1),round(mem_used_percent_size, 1), round(mem_available_size,1))

    URL = 'https://hooks.slack.com/services/' + args.key

    response = requests.post(URL, json={"text": message}) 



if __name__ == '__main__':
    alert = False
    while(True):
        if (check_local_state() or check_network_state()):
            alert = True

        if (alert):
            alert = False
            print("Message send...")
            send_alert()
        
        time.sleep(args.interval)

