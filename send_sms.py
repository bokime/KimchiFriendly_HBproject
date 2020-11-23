import os
from twilio.rest import Client


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
my_number = os.environ['MY_NUMBER']
twilio_number = os.environ['TEST_NUMBER']

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                        from_=twilio_number,
                        to=my_number
                        )

print(message.sid)