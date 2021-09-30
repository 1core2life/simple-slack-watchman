import requests 
import psutil
import time
from args import get_args


args = None
ALERT_CPU_PERCENT = None
ALERT_RAM_PERCENT = None
ALERT_URL = None

def get_system_state():
    cpu = psutil.cpu_percent(interval=0.1)
    mem_used_percent_size = psutil.virtual_memory().percent
    mem_available_size = psutil.virtual_memory().available/1204**3

    return cpu, mem_used_percent_size, mem_available_size


def check_local_state(cpu, mem_used_percent_size, mem_available_size):
    print("CPU: {0}% , RAM: {1}%, Available: {2} GB".format(round(cpu, 1),round(mem_used_percent_size, 1), round(mem_available_size,1)))

    if cpu > ALERT_CPU_PERCENT or mem_used_percent_size > ALERT_RAM_PERCENT:
        return True
    else:
        return False


def check_network_state():
    result = True

    if not ALERT_URL:
        URL = "http://127.0.0.1"
    else:
        URL = 'https://' + ALERT_URL

    try:
        response = requests.post(URL) 
        if response.status_code != 200:
            result = False
    except:
        result = False
        
    
    return result


def send_alert(cpu, mem_used_percent_size, mem_available_size):
    message = "CPU: {0}% , RAM: {1}%, Available: {2} GB".format(round(cpu, 1),round(mem_used_percent_size, 1), round(mem_available_size,1))

    URL = 'https://hooks.slack.com/services/' + args.key

    response = requests.post(URL, json={"text": message}) 



if __name__ == '__main__':
    args = get_args()

    ALERT_CPU_PERCENT = args.cpu
    ALERT_RAM_PERCENT = args.ram
    ALERT_URL = args.url

    alert = False
    while(True):
        cpu, mem_used_percent_size, mem_available_size = get_system_state()

        # Check Error State
        if (check_local_state(cpu, mem_used_percent_size, mem_available_size)):
            alert = True
        if (check_network_state()):
            alert = True


        # Send Error Message
        if (alert):
            alert = False
            print("Message send...")
            send_alert(cpu, mem_used_percent_size, mem_available_size)
        
        time.sleep(args.interval)

