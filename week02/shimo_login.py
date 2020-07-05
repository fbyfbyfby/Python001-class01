from selenium import webdriver
import time
try:
    browser = webdriver.Chrome()
    browser.get('https://shimo.im/')
    time.sleep(5)
    btn = browser.find_element_by_xpath(
        '//*[@id="homepage-header"]/nav/div[3]/a[2]/button')
    btn.click()
    browser.find_element_by_xpath(
        '//*[@name="mobileOrEmail"]').send_keys('fengboyang@sina.com')
    browser.find_element_by_xpath(
        '//*[@name="password"]').send_keys('a123456')
    time.sleep(3)
    btn = browser.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button')
    btn.click()
    cookies = browser.get_cookies()  
    print(cookies)

except Exception as e:
    print(e)
finally:
    time.sleep(10)
    browser.close()
