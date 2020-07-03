from selenium import webdriver
from getpass import getpass
from selenium.webdriver.chrome.service import Service


usr = input (" Enter ID ")
pwd = getpass (" ID Password ")
newpass = 54321

driver = webdriver.Chrome(executable_path='C:/Users/BlackTrack/Desktop/chromedriver.exe')
driver.get('http://lms.sustech.edu/login/index.php')


userbox = driver.find_element_by_id ('username')
userbox.send_keys (usr)

passbox = driver.find_element_by_id ('password')
passbox.send_keys (pwd)

loginbttn =driver.find_element_by_id ('loginbtn')
loginbttn.submit ()
#==========================================


passold = driver.find_element_by_id ('id_password')
passold.send_keys (pwd)

passnew1 = driver.find_element_by_id ('id_newpassword1')
passnew1.send_keys (newpass)

passnew2 = driver.find_element_by_id ('id_newpassword2')
passnew2.send_keys (newpass)

save =driver.find_element_by_id ('id_submitbutton')
save.submit ()

passbox.send_keys (pwd)
