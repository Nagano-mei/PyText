from twilio.rest import Client
import config

client = Client(config.account_sid, config.auth_token)

call = client.messages.create(
    to="+8615528363273",
    from_="+19093672680",
    body="This is our first message"
)

