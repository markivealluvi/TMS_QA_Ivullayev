import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_click_xpath():
    chrome = webdriver.Chrome('./chromedriver')
    try:
        url = 'https://ultimateqa.com/complicated-page/'
        chrome.get(url)
        time.sleep(2)

        button = chrome.find_element(By.XPATH, "//a[@class='et_pb_button et_pb_button_3 et_pb_bg_layout_light']")
        button.click()

    finally:
        chrome.quit()


def test_click_selector():
    chrome = webdriver.Chrome('./chromedriver')
    try:
        url = 'https://ultimateqa.com/complicated-page/'
        chrome.get(url)
        time.sleep(2)

        button = chrome.find_element(By.CSS_SELECTOR, "[class='et_pb_button et_pb_button_3 et_pb_bg_layout_light']")
        button.click()

    finally:
        chrome.quit()


def test_click_class():
    chrome = webdriver.Chrome('./chromedriver')
    try:
        url = 'https://ultimateqa.com/complicated-page/'
        chrome.get(url)
        time.sleep(2)

        button = chrome.find_element(By.CLASS_NAME, "et_pb_button.et_pb_button_3.et_pb_bg_layout_light")
        button.click()

    finally:
        chrome.quit()
