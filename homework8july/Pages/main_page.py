from homework8july.Pages.base_page import BasePage
from homework8july.Locators.locators import MainPageLocs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class MainPage(BasePage):

    def open_cart_page(self):
        time.sleep(2)
        WebDriverWait(self.chrome, 60).until(EC.presence_of_element_located(MainPageLocs.cart_button_loc))
        contact_link = WebDriverWait(self.chrome, 20).until(EC.element_to_be_clickable(MainPageLocs.cart_button_loc))
        contact_link.click()

    def verify_cart_link(self):
        time.sleep(2)
        assert self.is_element_present(MainPageLocs.cart_button_loc), "Cart link is not present!"