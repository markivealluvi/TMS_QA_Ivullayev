from selenium import webdriver
from selenium.webdriver.common.by import By


def test_dynamic_controls():

    chrome = webdriver.Chrome('./chromedriver')
    chrome.implicitly_wait(5)

    try:

        url = 'http://the-internet.herokuapp.com/frames'
        chrome.get(url)

        chrome.find_element(By.CSS_SELECTOR, '[href="/iframe"]').click()
        chrome.switch_to.frame(chrome.find_element(By.ID, 'mce_0_ifr'))
        text = chrome.find_element(By.XPATH, '//body/p').text
        assert text == 'Your content goes here.'

    finally:
        chrome.quit()
