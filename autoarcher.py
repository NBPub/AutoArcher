# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 15:01:36 2021

@author: NBPub
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
from base import Startup, Login, Navigator, unblockIP
from time import sleep

load_dotenv()
delay = int(os.environ.get("page_wait"))

driver = Startup()
print('Opening login page')
sleep(delay/2)

while driver.current_url.find('login') > 0:
    Login(driver)
    print('Logging in')
    sleep(1)

if driver.current_url.find('login') < 0:
    print('Navigating to page')
    sleep(delay)
    Navigator(driver)
    sleep(delay)
    
    print('Checking if a device is blocked')
    result = unblockIP(driver)
    print(result)
    
driver.quit()
