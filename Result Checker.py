# Credits - Shraddha Gore

# Import Libraries
import urllib.request
import os
import winsound
import ctypes
import re
import time
from bs4 import BeautifulSoup
from time import sleep

# Create an empty list for storing program codes
pcode = []

while True :
    # Message Box in Windows
    MessageBox = ctypes.windll.user32.MessageBoxW

    # Specify the URL
    mu_page = 'http://www.mumresults.in/'
    page = urllib.request.urlopen(mu_page)	

    # Parse the html using Beautiful Soup & store in 'soup'
    soup = BeautifulSoup(page, 'html.parser')

    # Get the program code 
    programCode_box = soup.find('table')
    for data in programCode_box.find_all('td', attrs={'class':'prgno'}) :
        code = data.text
        #print(code)

        # Add each code in list 
        pcode.append(code)

    #print(pcode)

    # Check for condition 
    if '\n 1T01017 \n' in pcode :
        # Play Windows Exit Sound
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

        # Display Windows Dialog Box
        MessageBox(None, 'RESULTS DECLARED!', ':)', 0)
        #print('RESULTS DECLARED!')
        quit()

    time.sleep(600)


# COMPS = '1T00717', EXTC - 1T01017

