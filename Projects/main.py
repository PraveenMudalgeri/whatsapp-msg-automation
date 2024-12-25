"""
twilio
datetime module
time module
"""
"""
Steps-
1 - twilio client setup
2 - user inputs
3 - scheduling logic
4 - send message
"""

#step 1 - install required libraries
from twilio.rest import Client #for sending whatsapp message
from datetime import datetime, timedelta #for managing date and time and time difference
import time  #to add delay

#step 2 - twilio credentials
account_sid = "" #your account sid
auth_token = "" #your auth token

client = Client(account_sid, auth_token)

#step 3 - define send message function
def send_whatsapp_message(recipient_number, message):
    try:
        message = client.messages.create(
            from_='whatsapp:', #your number
            body=message,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID: {message.sid}')
    except Exception as e:
        print('An error occured.')

#step - 4 User Inputs
name = input('Enter the recipient name: ')
recipient_number = input('Enter the recipient whatsapp number with country code: ')
message = input(f'Enter the message you want to send to {name}: ')

#step - 5 parse date/time and calculate delay
date_str = input('Enter the date to send the message (YYYY-MM-DD): ')
time_str = input('Enter the time to send the message (HH:MM in 24hr format): ')

#datetime module - to efficiently manage date and time management
sheduled_datetime = datetime.strptime(f'{date_str} {time_str}', '%Y-%m-%d %H:%M') #strptime - string parse time
current_datetime = datetime.now()

#calculate delay
time_diff = sheduled_datetime - current_datetime
delay_seconds = time_diff.total_seconds()

if delay_seconds <= 0:
    print('The specified time has already passed. Please enter a future time.')
else:
    print(f'Message scheduled to be sent to {name} at {sheduled_datetime}.')

    #wait until the scheduled time
    time.sleep(delay_seconds)

    #send the message
    send_whatsapp_message(recipient_number, message)