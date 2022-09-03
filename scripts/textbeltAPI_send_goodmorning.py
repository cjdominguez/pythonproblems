"""
By: Christian Dominguez
Friday September 2, 2022.

Script that sends a good morning text.

- API service - Textbelt which will send the message
- Requests Library - allows us to send requests to access an application
- Schedule Library - is a python library which allows you to schdeule a
  python script to run repeatedly aty a particular time.


"""
import requests
import schedule
import time

def send_text():

    resp = requests.post('https://textbelt.com/text', {
    'phone': '8134940188',
    'message': 'Hello world CJ',
    'key': 'textbelt',
    })
    print(resp.json())

schedule.every(1).day.at("19:10:00").do(send_text)

while True:

    schedule.run_pending()
    time.sleep(1)
