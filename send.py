from twilio.rest import Client
account_sid = ' '
auth_token = ''
client = Client(account_sid, auth_token)
def sendSms():
    message = client.messages.create(
    from_='[]',
    body='alert!!!!',
    to='[]'
    )

    print(message.sid)

 