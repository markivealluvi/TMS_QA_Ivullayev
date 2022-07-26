from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def test_dynamic_controls():

    chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    chrome.implicitly_wait(5)

    try:

        url = 'http://the-internet.herokuapp.com/dynamic_controls'
        chrome.get(url)

        chrome.find_element(By.CSS_SELECTOR, '[type="checkbox"]').click()
        chrome.find_element(By.CSS_SELECTOR, '[onclick="swapCheckbox()"]').click()
        chrome.find_element(By.ID, 'message')
        WebDriverWait(chrome, 5).until(EC.visibility_of_element_located((By.ID, 'message')))
        WebDriverWait(chrome, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '[type="checkbox"]')))

        input_text = chrome.find_element(By.CSS_SELECTOR, '[type="text"]')
        assert input_text.is_enabled() is False

        chrome.find_element(By.CSS_SELECTOR, '[onclick="swapInput()"]').click()
        WebDriverWait(chrome, 5).until(EC.visibility_of_element_located((By.XPATH, '//form[@id="input-example"]/p')))
        assert input_text.is_enabled() is True

    finally:
        chrome.quit()
