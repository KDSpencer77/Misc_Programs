# Send_SMS
# Coded using Python 3.7.0
# Uses the Twilio API

from twilio.rest import Client

number = "+19897084858"
message = "Hi there, I'm Python!"

client = Client("ACb7c817319f68bf9b86e92ac016401742",
                "73b2f269816876f69e6756114a071679")

client.messages.create(to=number,
                       from_="+15407014079",
                       body=message)
