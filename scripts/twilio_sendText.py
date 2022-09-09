"""

- created twilio account
- created .env file
- created .gitignore file
- recievied message on iphone

"""

import os

from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()



"""

eventually just the twilio interface

"""
account_sid = os.environ['TWILIO_ACCOUNT_SID'] # os.environ or os.getenv
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello World CJ - Twilio',
                              from_='+12182454422',
                              to='+18134940188'
                          )
print(message.sid)
