# Simple-Slack-Watchman

![Capture](https://i.imgur.com/SNr6pT2.png)

This is slack alarm bot for server monitoring

*Slack Webhook app is needed

<br/>
<br/>
<br/>

## How-To-Use
1. You can get Slack Webhook key by slack api guideline (https://api.slack.com/messaging/webhooks)  

2. In your local server, Execute watch.py

* ex) python watchman.py --key T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX --interval 10 --cpu 50 --ram 50

<br/>
<br/>
<br/>

## args
1. key : Slack WebHook key (hooks.slack.com/services/--key-----)
2. interval : Checking loop time
3. cpu : Limitation for cpu use percentage  
4. ram : Limitation for ram use percentage  

<br/>
<br/>
<br/>

## Requirement
* python
* psutil
* requests

