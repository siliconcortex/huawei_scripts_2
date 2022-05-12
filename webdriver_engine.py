import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
import shutil

def initialize():
  # your executable path is wherever you saved the chrome webdriver
  chromedriver = "C:\\Users\\lwx1025101\\Desktop\\WORKING DIRECTORY\\from_todoist\\chromedriver.exe"

  #auto download
  options = webdriver.ChromeOptions()
  prefs = {"profile.default_content_settings.popups": 0,
                "download.default_directory": r"C:\Users\lwx1025101\Desktop\WORKING DIRECTORY\from_todoist\\", # IMPORTANT - ENDING SLASH V IMPORTANT
                   "directory_upgrade": True}
  options.add_experimental_option("prefs", prefs)
  driver =  webdriver.Chrome(executable_path=chromedriver, options=options)  
  return driver

def initialize_headless():
    # your executable path is wherever you saved the chrome webdriver
    chromedriver = "C:\\Users\\lwx1025101\\Desktop\\WORKING DIRECTORY\\from_todoist\\chromedriver.exe"

    #auto download
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_settings.popups": 0,
                  "download.default_directory": r"C:\Users\lwx1025101\Desktop\WORKING DIRECTORY\from_todoist\\", # IMPORTANT - ENDING SLASH V IMPORTANT
                     "directory_upgrade": True}
    options.add_experimental_option("prefs", prefs)
    #chrome_options.add_argument("--disable-extensions")
    #chrome_options.add_argument("--disable-gpu")
    #chrome_options.add_argument("--no-sandbox") # linux only
    options.add_argument("--headless")
    # chrome_options.headless = True # also works
    driver =  webdriver.Chrome(executable_path=chromedriver, options=options)   
    return driver

# method to get the downloaded file name
def get_downloaded_file_name(driver, waitTime=10):
    driver.execute_script("window.open()")
    # switch to new tab
    driver.switch_to.window(driver.window_handles[-1])
    # navigate to chrome downloads
    driver.get('chrome://downloads')
    # define the endTime
    endTime = time.time()+waitTime
    while True:
        try:
            # get downloaded percentage
            downloadPercentage = driver.execute_script(
                "return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('#progress').value")
            # check if downloadPercentage is 100 (otherwise the script will keep waiting)
            if downloadPercentage == 100:
                # return the file name once the download is completed
                return driver.execute_script("return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('div#content  #file-link').text")
        except:
            pass
        time.sleep(1)
        if time.time() > endTime:
            break

def get_downloaded_file_name_2(path, newfilename):
  if not var:
    raise ("need to define filename")

  #filename = max([Initial_path + "\\" + f for f in os.listdir(Initial_path)],key=os.path.getctime)
  filename = max([os.path.join(path, f) for f in os.listdir(Initial_path)], key=os.path.getctime)
  shutil.move(filename,os.path.join(path,newfilename))