3from selenium import webdriver
from getpass import getpass
from selenium.webdriver.chrome.service import Service


usr = input (" Enter ID ")
pwd = getpass (" ID Password ")


driver = webdriver.Chrome(executable_path='---')  #<---Put chromedriver.exe Path Here--->#
driver.get('---') #<---Website Link Here--->#


userbox = driver.find_element_by_id ('---')  #<---Element Here--->#
userbox.send_keys (usr)

passbox = driver.find_element_by_id ('---')  #<---Element Here--->#
passbox.send_keys (pwd) 

loginbttn =driver.find_element_by_id ('---') #<---Element Here--->#
loginbttn.submit ()
#==========================================



