from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from functools import wraps
import time
from selenium.webdriver.chrome.options import Options
# class makemytrip():
#     def flight_booking(self):
#         driver=webdriver.Chrome()
#         driver.get("https://www.makemytrip.com/")
#         driver.maximize_window()
#         #driver.save_screenshot("screenshot.png")
#         driver.implicitly_wait(10)
#         driver.find_element_by_xpath('//*[@id="SW"]/div[1]/div[1]/ul/li[6]').click()
#         driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[1]').click()
#         driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/input').send_keys('Mumbai')
#         driver.find_element_by_xpath('//*[@id="react-autowhatever-1-section-0-item-0"]/div/div[1]').click()
#         driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[2]').click()
#         driver.implicitly_wait(5)
#         driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div/input').send_keys('Hyderbad')
#         driver.implicitly_wait(5)
#         driver.find_element_by_xpath('//*[@id="react-autowhatever-1-section-0-item-0"]/div').click()
#         driver.implicitly_wait(5)
#         driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[3]').click()
#         s=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[3]').text
#         print(s.split())
#         book = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div[5]/div[5]/div')
#         book.click()
#         driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[4]').click()
#         driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div[5]/div[6]/div').click()
#         search=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/p/a')
#         a=search.text
#         assert a == 'SEARCH','string not matching'
#
#         search.click()
# obj=makemytrip()
# obj.flight_booking()

#
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('http://www.w3schools.com/')
target = driver.find_element_by_link_text('LEARN PYTHON')
actions = ActionChains(driver)
actions.move_to_element(target)
actions.perform()
target.click()
#
# # driver = webdriver.Chrome()
# # driver.get('http://www.w3schools.com/')
# # target = driver.find_element_by_link_text('BROWSE TEMPLATES')
# # c=target.location_once_scrolled_into_view()
# seq = driver.find_elements_by_tag_name('iframe')
# d=driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div').text
# print(list(d.split()))
#
# print("No of frames present in the web page are: ", len(seq))


# go to Google and click the I'm Feeling Lucky button


# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import os
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=1920x1080")
#
# # download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# # current directory
# chrome_driver = os.getcwd() +"\\chromedriver.exe"
# driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
# driver.get("https://www.google.com")
# lucky_button = driver.find_element_by_css_selector("[name=btnI]")
# lucky_button.click()
#
# # capture the screen
# driver.get_screenshot_as_file("capture.png")



from datetime import datetime

from selenium import webdriver

# driver=webdriver.Chrome()
# try:
#         driver.get("https://www.makemytrip.com/")
#         driver.maximize_window()
#         search = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/p/a')
#         a=search.text
#         assert a == 'SEARC','string not matching'
#         search.click()
#
# except Exception as e:
#
#     print(e)
#
#     now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#
#     driver.get_screenshot_as_file('screenshot-%s.png' % now)
from datetime import datetime

# def screenshot_on_failure(function_to_call):
#     """
#     Decorator to take screen shot on test case failure.
#
#     :param function_to_call: Function to be called in this decorator
#     :return: function_wrapper instance
#     """
#     @wraps(function_to_call)
#     def function_wrapper():
#         try:
#             function_to_call()
#         except Exception:
#             now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#             driver.get_screenshot_as_file('screenshot-%s.png' % now)
#             raise
#     return function_wrapper
#
#
# @screenshot_on_failure
# def failer():
#     global driver
#     driver = webdriver.Chrome()
#
#     driver.get("https://www.makemytrip.com/")
#     driver.maximize_window()
#     search = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/p/a')
#     a = search.text
#     assert a == 'SEARCH', 'string not matching'
#     search.click()
#
# failer()