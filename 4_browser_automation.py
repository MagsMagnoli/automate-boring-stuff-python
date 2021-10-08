from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://automatetheboringstuff.com')
elem = browser.find_element_by_css_selector('#id')
elem.click()