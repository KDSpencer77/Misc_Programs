# Message_Spammer
# Coded using Python 3.7.0

import datetime
from datetime import date
from twilio.rest import Client

# Function Definition
def DateCalc(Date_1, Date_2):
    d1 = Date_1
    d2 = Date_2
    result = d2 - d1
    return result

def SendSMS(number, text):
    client = Client("ACb7c817319f68bf9b86e92ac016401742",
                    "73b2f269816876f69e6756114a071679")
    client.messages.create(to=number,
                           from_="+15407014079",
                           body=text)

# Variable Definition
ProgramState = 1

if ProgramState == 1:
    phone_numbers = ["+19894656056"]

else:
    phone_numbers = ["+19894656056",  # Mom
                     "+19894953367",  # Dad
                     "+19894953453"]  # Katie

current_date = datetime.datetime.now()
target_date = datetime.datetime(2020, 12, 25)

num_of_days = DateCalc(current_date, target_date)

# Main Body
day_num = num_of_days.__str__()
day_num = day_num.split()
day_num = day_num[0]

message = "Days Till Christmas: " + day_num
print(message)

for num in phone_numbers:
    print("Texting: ", num)
    #SendSMS(num, message)
