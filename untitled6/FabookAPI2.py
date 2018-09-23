from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
if __name__ == "__main__":
    service_args = ['--proxy=localhost:9150', '--proxy-type=socks5' ]
    driver = webdriver.PhantomJS(executable_path="/Users/cankincal/Desktop/phantomjs-2.1.1-macosx/bin/phantomjs",service_args=service_args)
    driver.get("http://www.facebook.com")
    email = driver.find_element_by_id("email")
    password = driver.find_element_by_id("pass")
    email.send_keys("dj_cvb_can_26@hotmai.com")
    password.send_keys("05062043224a")
    password.send_keys(Keys.RETURN)
    time.sleep(3)
    driver.get('https://www.facebook.com/bilginerhan')
    print(driver.find_element_by_id("content").text)
    print(driver.find_element_by_tag_name("div"))
    print(driver.find_element_by_css_selector("#content"))
   # driver.get("http://www.facebook.com/messages/")

