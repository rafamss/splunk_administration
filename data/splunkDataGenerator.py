import random
import json
import logging
import sys
import os
import time
from datetime import datetime

def commitCrime():

    # list of sample values
    suspect = ['Miss Scarett','Professor Plum','Miss Peacock','Mr. Green','Colonel Mustard','Mrs. White', 'Mr. Red', 'Mr. Gates', 'Young Peter', 'Young Claire', 'Grandpa Ray', 'Grandma Shonda', 'Nurse Ane']
    weapons = ['candlestick','knife','lead pipe','revolver','rope','wrench','baseball bat', 'punch', 'harmonica','sword', 'rock']
    actions = ['success','attempt','fail','canceled','arrested','contained']
    crime_types = ['single','multiple','violent','property','organized','white-collar']
    victims = ['John Lister','Ama Holly','Paul Lence','Jessica Mon','Billy Horn','Shonda MCals','Michael Anothony','Geff Gutemberg','Alonso Aguiar','Hugo Martinez']
    rooms = ['kitchen','ballroom','conservatory','dining room','cellar','billiard room','library','lounge','hall','study','swimming pool', 'living room', 'basement', 'garage','game room']
    periods_day = ['afternoon','bedtime','dinnertime','lunchtime','morning','dawn']
    curr_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    return {"timestamp":curr_time,"suspect":random.choice(suspect), "weapon":random.choice(weapons), "location":random.choice(rooms), "period of the day":random.choice(periods_day), "victim":random.choice(victims), "crime_type":random.choice(crime_types), "action":random.choice(actions)}

path= 'C:/Users/Splunk/Desktop/continuous_log.txt'
# filetxt = open(path, 'w')
# read = filetxt.read()
# print(read)

i = 1
while 'splunk'!='splank':
    filetxt = open(path, 'a')
    event = commitCrime()
#   event.update({"action":"success"})
#   event.update({"crime_type":"single"})
    event.update({"crime_number":i})
    filetxt.write(json.dumps(event))
    filetxt.write("\n")
    i += 1
    time.sleep(.3)
filetxt.close()
