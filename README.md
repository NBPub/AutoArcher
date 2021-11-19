# AutoArcher
Python-Selenium example(s) to work with Archer router pages. Code can be used as a start to building one's own automated Archer process. Tested on Archer A7 aka C7 with Chromium driver.

## Usage
To be added. Install in venv / poetry.

### Installation

### .env File

### Webdrivers, Selenium
This example uses Chromium drivers and has been tested on Windows 10, OS X, and Debian. See section 1.5 of the [Selenium Installation Docs](https://selenium-python.readthedocs.io/installation.html) for more information on downloading and installing broswer drivers. If another driver is used, minor adjustments would be required in the code. I could allow a setting in the ENV file to allow for browser agnosticism.

#### Webdriver easy examples
Conda ex, Debian ex

### Adjustments

## Current Example
The current example serves to:
1. Log in
2. Navigate to Advanced Settings Tab
3. From there > Security > Settings
4. Check if listed IPs are being blocked (Blocked DoS Host List)
5. Delete listed IPs from blocklist, if present. If another IP is present, the script terminates.

## Personal Motivation
With my current settings, local Apple devices are occasionally added to the block list (and stop receiving WiFi). I made this to automate removal of these devices.

## General Motivation
* Share Selenium tricks I picked up in this process. I will go back and find+list links of blog posts, etc . . . that helped me.
* Provide examples for working with Archer router pages
* Get feedback
