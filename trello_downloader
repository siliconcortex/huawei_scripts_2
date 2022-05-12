import requests
from selenium import webdriver
from combine_csv import combine_csv, delete_csv
from time import sleep
from webdriver_engine import initialize, initialize_headless

import logging
from datetime import date

long_wait = 10
short_wait = 5
very_short_wait = 1
download_wait = 20

if name == 'main':
  def initialize_logging():
    logfile_filename = "logfile_todoist_batch_download" + str(date.today()) + ".txt"
    logging.basicConfig(level=logging.INFO, filename=logfile_filename, filemode="a+",
              format="%(asctime)-15s %(levelname)-8s %(message)s")
    logging.info("starting todoist batch download...")

    
  initialize_logging()
  #run initialization of the driver
  logging.info("initializing webdriver")
  driver = initialize()

  logging.info("deleting existing files")
  delete_csv("LTE")
  delete_csv("todoist_merged_")

  logging.info("opening browser...")
  url1 = "https://todoist.com"
  driver.get(url1)

  #wait for the page to load


  driver.implicitly_wait(short_wait)

  #find login button and click it
  logging.info("logging in...")
  login_button = driver.find_element_by_link_text("Log in")
  login_button.click()

  driver.implicitly_wait(short_wait)

  #type credentials
  email_textbox = driver.find_element_by_id("element-0")
  password_textbox = driver.find_element_by_id("element-2")
  login_submit_button = driver.find_element_by_css_selector('button[class="_7a2031d6 a878a9a4 _34ac3da9 f9408a0e _8c75067a"]')

  #type in login credentials
  email_textbox.send_keys("lesliecaminade@gmail.com")
  driver.implicitly_wait(very_short_wait)
  password_textbox.send_keys("yourkungfuisweak")
  driver.implicitly_wait(very_short_wait)
  login_submit_button.click()

  sleep(2)

  #list of urls to download
  urls = [
  "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2270750854&use_relative_dates=0", # 1 to 4
  "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2270731118&use_relative_dates=0", 
  "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2271534070&use_relative_dates=0",
  "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2271539103&use_relative_dates=0",
  "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2275958553&use_relative_dates=0", #6 to 10
  "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2275959010&use_relative_dates=0",
  "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2275959391&use_relative_dates=0",
  "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2275959804&use_relative_dates=0",
  "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2275960207&use_relative_dates=0",
  "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2273955814&use_relative_dates=0", #5G
  "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2276285137&use_relative_dates=0", #CRITICAL AND HU WK40
  "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2276197819&use_relative_dates=0", #Searoute
  "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2276376301&use_relative_dates=0", #Pending Sectors
  "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2276572931&use_relative_dates=0", #mos done rem oct 23
  "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2276978506&use_relative_dates=0", #277 sites addl
  "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2277075271&use_relative_dates=0", #2g 3g
  "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2277513983&use_relative_dates=0", #add nov 2
  "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2278217561&use_relative_dates=0", #L2100 544 REMAINING
  # "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2281463096&use_relative_dates=0", #q1 forecast critical 2022 sector levels
  # "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2281463362&use_relative_dates=0",
  # "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2281463407&use_relative_dates=0",
  # "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2281463469&use_relative_dates=0",
  # "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2281463529&use_relative_dates=0",

  "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2284614232&use_relative_dates=0", #remaining 5g 

  "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2286189379&use_relative_dates=0", #pending SV march 2022 
  "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2286773679&use_relative_dates=0", #lte expansion 11 - add march 11 2022

  "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2287002652&use_relative_dates=0", #zone 9 PAT
  "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2287002645&use_relative_dates=0", #zone 9 implem

  "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2287152533&use_relative_dates=0", #zone 9 possible backlog
  "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2287514390&use_relative_dates=0", #zone 9 additional pat 2

  "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2290203897&use_relative_dates=0", #zone 3 april
  "https://todoist.com/API/v8.7/templates/export_as_file?project_id=2290534395&use_relative_dates=0", #zone 1 april
  ]

  #visit and download each csv file one by one 
  logging.info("downloading files...")
  count = 0
  for url in urls:
    count = count + 1
    logging.info(f"""file {count} of {len(urls)}...""")
    driver.get(url)
    driver.implicitly_wait(download_wait)

  #close the webdriver
  sleep(round(2 * len(urls)))
  driver.close()
  driver.quit()

  #merge the files
  logging.info("merging files...")
  path = ""
  input_filename = "LTE*.csv"
  output_filename = f"""todoist_merged_{str(date.today())}.csv"""
  combine_csv(input_filename, output_filename, path)

  logging.info("done.")