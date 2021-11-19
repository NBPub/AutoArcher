# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 14:42:22 2021

@author: NBPub
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
from dotenv import load_dotenv
from os import environ

# Load data from ".env", default values provided if environmental variables not set.
load_dotenv()
page = environ.get('router_address','http://192.168.1.1')
password = environ.get("router_pass",'password')
IPs = environ.get("IPs",'0').split(',')
Devices = environ.get("Devices",'?').split(',')

# Add dummy device names if lengths don't match
if len(Devices) != len(IPs):
    Devices = ['?']*len(IPs)

# Load router page
def Startup():
    driver = webdriver.Chrome()
    driver.get(page)
    assert "Archer A7" in driver.title # Likely unnecessary, but it feels good to make sure
    return driver

# Enter password and login
def Login(driver):
    elem = driver.find_element(By.XPATH, "//div") # Random spot within screen to click
    
    # As password field element cannot be selected, click outside and then "tab" into it
    action = ActionChains(driver)
    action.move_to_element(elem)
    action.send_keys(key.TAB) # Tab to get into password field
    action.send_keys(password)
    action.send_keys(key.PASSWORD) # Enter to advance
    action.perform()
    del action, elem

# Move to desired page, in this case Advanced Security Settings
def Navigator(driver):
    driver.implicitly_wait(10) # Not sure if this helps, I have not figured out "waiting" and use time.sleep's
    
    # Advanced Tab
    elem0 = driver.find_element(By.XPATH, "//a[@name='advanced']")
    elem0.click()
    del elem0
    sleep(5)
    
    # Optional: Scroll down to make Security link interactable, for low-res windows. Elem name may need adjustment based on page.
    # Names could be "Status", "Network", "Wireless", etc . . .
    # elem = driver.find_element_by_xpath("//a[@name='qos']")
    # action = ActionChains(driver)
    # action.move_to_element_with_offset(elem,230,0)
    # action.click()
    # action.perform()
    # del action, elem
    # sleep(3)
        
    # Click Security Settings, reveal link
    elem1 = driver.find_element(By.XPATH, "//a[@name='security']")
    elem1.click()
    del elem1
    sleep(1)
    
    # Go to Security Settings
    elem2 = driver.find_element(By.XPATH, "//a[@name='settings'][@class='sec']")
    elem2.click()
    del elem2
    sleep(1)

# Check if blocked IPs are in list, unblock if so.
# If IP is present that is not in list, the program ends. In my case, I'd want to see what is being blocked manually.
# If no IPs are present, program terminates. If another error is raised, it will be printed.
def unblockIP(driver):
    driver.implicitly_wait(10)
    while True:
        try:
            IP = driver.find_element(By.XPATH, "//td[@name='ipaddr']").text
        except Exception as e:
            etext = str(e)
            if etext[0:24] == 'Message: no such element':
                return 'No (more) IPs being blocked'
            else:
                return etext    
        
        if IP in IPs:
            device = Devices[IPs.index(IP)]    
            print(f'{device} is being blocked, unblocking . . .')
            
            # Hit checkbox
            elem3 = driver.find_element(By.XPATH, "//td[@name='check-column']")
            elem3.click()
            del elem3
            sleep(1)        
                
            # Hit delete button
            elem4 = driver.find_element(By.CLASS, 'btn-delete')
            elem4.click()
            del elem4
            sleep(2)
            
            # Navigate to OK and click
            headers = driver.find_elements(By.XPATH, "//h4[@class='title']")
            elem5 = headers[5]
            action = ActionChains(driver)
            action.move_to_element(elem5)
            action.move_by_offset(110,80) # Not sure how general this move-by-offset will be. Adjustments may be required.
            action.click()
            action.perform()
            print(f'Success! {IP} aka {device} unblocked.')
            sleep(2)
            
        else:
            return f'Another IP is being blocked: {IP}'
