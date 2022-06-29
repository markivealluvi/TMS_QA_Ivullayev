import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_filling_forms_1():
    chrome = webdriver.Chrome('./chromedriver')
    try:
        url = 'https://ultimateqa.com/filling-out-forms/'
        chrome.get(url)
        time.sleep(2)

        input_name = chrome.find_element(By.ID, 'et_pb_contact_name_0')
        name = 'Ikram'
        input_name.send_keys(name)

        input_message = chrome.find_element(By.ID, 'et_pb_contact_message_0')
        message = 'Hello world!'
        input_message.send_keys(message)

        submit_button = chrome.find_element(By.XPATH, "(//button[@type='submit'])[1]")
        submit_button.click()
        time.sleep(2)
        message2 = chrome.find_element(By.XPATH, "//div[@class='et-pb-contact-message']/p")

        assert message2.is_displayed()
    finally:
        chrome.quit()


def test_filling_forms_2():
    chrome = webdriver.Chrome('./chromedriver')
    try:
        url = 'https://ultimateqa.com/filling-out-forms/'
        chrome.get(url)
        time.sleep(2)

        input_name = chrome.find_element(By.ID, 'et_pb_contact_name_0')
        name = 'Ikram'
        input_name.send_keys(name)

        submit_button = chrome.find_element(By.XPATH, "(//button[@type='submit'])[1]")
        submit_button.click()
        time.sleep(2)
        message2 = chrome.find_element(By.XPATH, "//div[@class='et-pb-contact-message']/p")

        assert message2.is_displayed()

    finally:
        chrome.quit()


def test_filling_forms_3():
    chrome = webdriver.Chrome('./chromedriver')
    try:
        url = 'https://ultimateqa.com/filling-out-forms/'
        chrome.get(url)
        time.sleep(2)

        input_message = chrome.find_element(By.ID, 'et_pb_contact_message_0')
        message = 'Hello world!'
        input_message.send_keys(message)

        submit_button = chrome.find_element(By.XPATH, "(//button[@type='submit'])[1]")
        submit_button.click()
        time.sleep(2)
        message2 = chrome.find_element(By.XPATH, "//div[@class='et-pb-contact-message']/p")

        assert message2.is_displayed()

    finally:
        chrome.quit()
