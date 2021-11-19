# AutoArcher
Python-Selenium example(s) to work with Archer router pages. Code can be used as a start to building one's own automated Archer process. Tested on Archer A7/C7 with Chromium driver.


## Personal Motivation
With my current settings, local Apple devices are occasionally added to the block list (and stop receiving WiFi). I made this to automate removal of these devices.

## General Motivation
* Share Selenium tricks I picked up in this process. I will go back and find+list links of blog posts, etc . . . that helped me.
* Provide examples for working with Archer router pages
* Get feedback

## Installation
*[Python 3.5 or later](https://wiki.python.org/moin/BeginnersGuide/Download) is required for Poetry.* 

See [Poetry Docs](https://python-poetry.org/docs/) for more details.

1. Install Poetry, see above link for guidance.
2. [Download](https://github.com/NBPub/AutoArcher/archive/refs/heads/main.zip) AutoArcher code, see green **Code** button at top of page for more options.
3. Extract contents to directory of choice. READEME.md, LICENSE, and .gitignore files are not necessary.
4. Modify "example.env" as [described](https://github.com/NBPub/AutoArcher#env-file). Rename to ".env"
5. Install webdrivers for Selenium. See [below](https://github.com/NBPub/AutoArcher#webdrivers-selenium).
6. Navigate to folder in terminal, install dependencies (first time only), and run script.

```
cd choice-directory
poetry install
poetry run autoarcher.py
```
6. Program outputs are output to terminal window.

## Usage

### .env File
Certain parameters are sent to the code via a file called ".env", located in the same directory. An example is provided ["example.env"](https://github.com/NBPub/AutoArcher/blob/main/example.env). Simply adjust the values in the example, and then remove "example" from the file name.

### Webdrivers, Selenium
This example uses [Chromium drivers](https://sites.google.com/chromium.org/driver/) and has been tested on Windows 10, OS X, and Debian. See section 1.5 of the [Selenium Installation Docs](https://selenium-python.readthedocs.io/installation.html) for more information on downloading and installing broswer drivers. 

If another driver is used, minor adjustments would be required in the code. I could allow a setting in the ENV file to allow for browser agnosticism.

**Easy examples**
* Anaconda/Conda - Install "chromedriver-binary" package
* Debian ([source](https://ivanderevianko.com/2020/01/selenium-chromedriver-for-raspberrypi)) - "sudo apt-get install chromium-chromedriver" 
* [MAC Instructions](https://www.swtestacademy.com/install-chrome-driver-on-mac/) - good details and background

### Adjustments
As mentioned within the code's comments, I do not yet have a good grasp of **Waits** in Selenium. Therefore I use a bunch of time.sleep(x) commands to ensure pages load before moving to a next step. These times may need to be adjusted for a particular machine.


## Current Example
The current example serves to:
1. Log in
2. Navigate to Advanced Settings Tab
3. From there > Security > Settings
4. Check if listed IPs are being blocked (Blocked DoS Host List)
5. Delete listed IPs from blocklist, if present. If another IP is present, the script terminates.

*Output if no IPs are being blocked*

![Home](/output_example.png "Output")
