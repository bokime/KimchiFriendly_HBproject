# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
my_number = os.environ['MY_NUMBER']
twilio_number = os.environ['TWILIO_NUMBER']


client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="Hello! Your neighbor requested your Kimchi jar share!",
                    from_=twilio_number,
                    to=my_number
                    )

print(message.sid)
