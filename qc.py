from selenium import webdriver
import sys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

user = str(sys.argv[1])
pwd = str(sys.argv[2])
driver = webdriver.Chrome()
driver.get("https://secure.quikchex.in/users/sign_in")
assert "Sign In" in driver.title

elem = driver.find_element_by_id("user_email")
elem.send_keys(user)
elem = driver.find_element_by_id("user_password")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

time.sleep(20)
elm = driver.find_element_by_link_text('Mark Attendance')
elm.click()

print """ 

   _________________________________
  |:::::::::::::;;::::::::::::::::::|
  |:::::::::::'~||~~~``:::::::::::::|
  |::::::::'   .':     o`:::::::::::|
  |:::::::' oo | |o  o    ::::::::::|
  |::::::: 8  .'.'    8 o  :::::::::|
  |::::::: 8  | |     8    :::::::::|
  |::::::: _._| |_,...8    :::::::::|
  |::::::'~--.   .--. `.   `::::::::|
  |:::::'     =8     ~  \ o ::::::::|
  |::::'       8._ 88.   \ o::::::::|
  |:::'   __. ,.ooo~~.    \ o`::::::|
  |:::   . -. 88`78o/:     \  `:::::|
  |::'     /. o o \ ::      \88`::::|   "You will join us or die."
  |:;     o|| 8 8 |d.        `8 `:::|
  |:.       - ^ ^ -'           `-`::|
  |::.                          .:::|
  |:::::.....           ::'     ``::|   "==================================="
  |::::::::-'`-        88          `|   |                                   |
  |:::::-'.          -       ::     |   |   Attendance Marked Like a Boss   |
  |:-~. . .                   :     |   |                                   |
  | .. .   ..:   o:8      88o       |   "==================================="
  |. .     :::   8:P     d888. . .  |
  |.   .   :88   88      888'  . .  |
  |   o8  d88P . 88   ' d88P   ..   |
  |  88P  888   d8P   ' 888         |
  |   8  d88P.'d:8  .- dP~ o8       |   Darth Vader thanks Rv
  |      888   888    d~ o888    LS |
  |_________________________________|

"""
driver.close()
