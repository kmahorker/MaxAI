#Variables
import os
dir(os)
import pywapi
import string
from random import choice
import urllib
import re
import time

# Voice Recognition
#subprocess.call(['say','testing'])

#Loop
person = "Daniel"
for i in range(10000000):
    set1=["Yes","Maybe","No"]
    set2=["Do not question my intelligence.", "Your question could not be understood. Please try again later.", "Excuse me?","Please wait... Your question cannot be processed."]
    question = raw_input("What would you like to ask Max? ")
    answer =''
    symbol = ''
    zipCode = ''
    talk = os.system('say "%s"' % answer)
    voice = ''
    api_key = ''
    
# Questions
    if question=="What is your name?":
        answer= "My name is Max."
    elif question == "How old are you?":
        answer='I was born on July 25,2012'
    elif "Are" in question:
        answer=choice(set1)
    elif "Is" in question:
        answer = choice(set1)
    elif "Does this" in question:
        answer = choice(set1)
    #elif "Can" in question:
    #    answer = choice(set1)
    elif "Do" in question:
        answer = choice(set1)
    elif "Does" in question:
        answer = choice(set1)
    elif "May" in question:
        answer = choice(set1)
    elif "Could" in question:
        answer = choice(set1)
    elif "Did" in question:
        answer = choice(set1)
    elif "Will" in question:
        answer = choice(set1)
    elif "So" in question:
        answer = choice(set1)
    elif "So what" in question:
        answer = choice(set2)
    elif "time" in question:
        answer = time.strftime('%l:%M%p on %b %d, %Y')
    
# Google Weather API
    elif question == "What is the weather?":
        os.system('say "%s"' % "What is your zip code?")
        zipCode = raw_input("What is your zip code?")
        google_result = pywapi.get_weather_from_google(zipCode)
        answer = "It's " + string.lower(google_result['current_conditions']['condition']) + " and " + google_result['current_conditions']['temp_f'] + " degrees Fahrenheit. \n\n"
        print answer
        os.system('say "%s"' % answer)
        os.system('say "%s"' % "Would you like Celsius?")
        celsius = raw_input("Would you like Celsius? ")
        
        if "yes" in celsius:
                answer = "It's " + string.lower(google_result['current_conditions']['condition']) + " and " + google_result['current_conditions']['temp_c'] + " degrees Celsius. \n\n"
        elif "Yes" in celsius:
                answer = "It's " + string.lower(google_result['current_conditions']['condition']) + " and " + google_result['current_conditions']['temp_c'] + " degrees Celsius. \n\n"
        elif "Sure" in celsius:
                answer = "It's " + string.lower(google_result['current_conditions']['condition']) + " and " + google_result['current_conditions']['temp_c'] + " degrees Celsius. \n\n"
        else:
            answer = ''

# Stocks API
    elif question == "What is the stock?":
        symbol = raw_input("What is the stock name?")
        base_url = 'http://finance.google.com/finance?q='
        content = urllib.urlopen(base_url + symbol).read()
        m = re.search('id="ref_694653_l".*?>(.*?)<', content)
        if m:
            quote = m.group(1)
        else:
            quote = 'no quote available for: ' + symbol
        print "$" + quote
        os.system('say "%s"' % "$" + quote)

# Current Location
    elif question =="Where am I?":
        from googlemaps import GoogleMaps
        gmaps = GoogleMaps(api_key)
        address = reverse['Placemark'][0]['address']
        lat, lng = gmaps.address_to_latlng(address)
        destination = gmaps.latlng_to_address(lat,lng)
        print destination
        
# Change Voice
    elif question == "Can you talk differently?":
        voice = raw_input("Would you like me to be male or female? ")
        if voice == "male" or voice == "Male":
            person = "Alex" 
        elif voice == "female" or voice == "Female":
            person = "Vicki" 
    else:
        answer = choice(set2)
        if question == '':
            answer = ''

# Final Commands
    print answer
    if person == "Daniel":
        os.system('say "%s" "-v" "Daniel"' % answer)
    if person == "Vicki":
        os.system('say "%s" "-v" "Vicki"' % answer)
    if person == "Alex":
        os.system('say "%s" "-v" "Alex"' % answer)
