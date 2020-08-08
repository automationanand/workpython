import math

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

def testsquare():
   num = 7
   assert 7*7 == 49

def testquality_test():
   assert 10 == 10


# import os
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# # Headless browser
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(executable_path=r"C:/Users/Dell/Desktop/PANDAS/chromedriver.exe", chrome_options=chrome_options)
#
# driver.get('http://www.w3schools.com/')
# target = driver.find_element_by_link_text('LEARN PYTHON')
# actions = ActionChains(driver)
# actions.move_to_element(target)
# actions.perform()
# print("successfull with headless browser")
# target.click()