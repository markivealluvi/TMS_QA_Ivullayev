import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_select():
    chrome = webdriver.Chrome('./chromedriver')
    try:
        url = 'http://demo.guru99.com/test/newtours/register.php'
        chrome.get(url)
        time.sleep(2)

        first_name = chrome.find_element(By.NAME, 'firstName')
        name = 'Ikram'
        first_name.send_keys(name)

        last_name = chrome.find_element(By.NAME, 'lastName')
        family_name = 'Ivullayev'
        last_name.send_keys(family_name)

        phone_number = chrome.find_element(By.NAME, 'phone')
        phone = '87479821410'
        phone_number.send_keys(phone)

        email = chrome.find_element(By.NAME, 'userName')
        e_mail = 'ikram@gmail.com'
        email.send_keys(e_mail)

        address = chrome.find_element(By.NAME, 'address1')
        addr = 'Kima, 19'
        address.send_keys(addr)

        city_name = chrome.find_element(By.NAME, 'city')
        city = 'Almaty'
        city_name.send_keys(city)

        province = chrome.find_element(By.NAME, 'state')
        province.send_keys(city)

        postcode = chrome.find_element(By.NAME, 'postalCode')
        post_code = '142536'
        postcode.send_keys(post_code)

        country = Select(chrome.find_element(By.NAME, 'country'))
        country.select_by_value('KAZAKHSTAN')

        user_name = chrome.find_element(By.NAME, 'email')
        username = 'markivealluvi'
        user_name.send_keys(username)

        password = chrome.find_element(By.NAME, 'password')
        password.send_keys('qwerty123')

        conf_password = chrome.find_element(By.NAME, 'confirmPassword')
        conf_password.send_keys('qwerty123')

        time.sleep(3)

        submit_button = chrome.find_element(By.NAME, 'submit')
        submit_button.click()

        fullname_check = chrome.find_element(By.XPATH, '(.//tr//table//font)[4]').text
        assert name, family_name in fullname_check

        username_check = chrome.find_element(By.XPATH, '(.//tr//table//font)[6]').text
        assert username in username_check

    finally:
        chrome.quit()
