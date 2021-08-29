
import time
from selenium import webdriver

#Initializing Firefox web browser
driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")

#open Comtravo website
driver.get("https://my.qa.comtravo.it/auth/login")
time.sleep(2)

#Enter Login User details
driver.find_element_by_css_selector("input[type='email']").send_keys("robot+qatask@comtravo.com")
time.sleep(1)

#Enter Password
driver.find_element_by_name("password").send_keys("Qatask@08")
time.sleep(1)

#Click on SignIn Button
LogIn = driver.find_element_by_css_selector("button[type='submit']").click()
time.sleep(6)

#Click on Select Traveler
driver.find_element_by_css_selector("input[placeholder='Select travelers']").send_keys("Sophie")
time.sleep(2)

#Select 'sophie lie' from the list
driver.find_element_by_css_selector("p[data-cy='Sophie']").click()
time.sleep(2)

#Click on departure
Departure = driver.find_element_by_css_selector("input[placeholder='Departure']").send_keys("BER")
time.sleep(2)
#Select Berlin from the Departure list
driver.find_element_by_css_selector("div[data-cy='Berlin Brandenburg']").click()
time.sleep(2)


#Click on destination
Destination = driver.find_element_by_css_selector("input[placeholder='Destination']").send_keys("MUC")
time.sleep(2)
#Select Munich from the Destination list
driver.find_element_by_css_selector("div[data-cy ='Franz Josef Strauss']").click()
time.sleep(2)


#Click on Calender Icon
driver.find_element_by_css_selector("ctr-input-datepicker[placement='left']").click()
time.sleep(2)

#Click on the right arrow button of the calendar
Arrow=driver.find_element_by_xpath("//div[@class='ctr-datepicker']/div[1]/div[2]/ctr-calendar/div[1]/ctr-header/div[1]/div[4]")
Arrow.click()
time.sleep(2)

#Select date[30] from October Month
Date=driver.find_element_by_xpath("//div[@class='ctr-overlay']/div[2]/ctr-datepicker/div[1]/div[1]/div[2]/ctr-calendar/div[1]/ctr-month/div[34]")
Date.click()

#Select date[31] from October Month
Date1=driver.find_element_by_xpath("//div[@class='ctr-overlay']/div[2]/ctr-datepicker/div[1]/div[1]/div[2]/ctr-calendar/div[1]/ctr-month/div[35]")
Date1.click()
time.sleep(2)

#Click on search flight button
FlightButton = driver.find_element_by_xpath("//button[@data-cy='Search flights']")
FlightButton.click()
time.sleep(20)

#Click on the very first option of Select
SearchButton = driver.find_element_by_xpath("//div[@class='col']/div[1]/ctr-item-card[1]/ctr-card/div/div/div[1]/div[1]/ctr-item-card-info/div/div[2]/button")
SearchButton.click()
time.sleep(4)

#Click on Book this Trip Button
BookThisTrip = driver.find_element_by_css_selector("button[aria-label='book this flight option']")
BookThisTrip.click()

time.sleep(10)

driver.close()


