from homework8july.Pages.base_page import BasePage
from homework8july.Locators.locators import CartPageLocs


class CartPage(BasePage):

    def verify_title_is_present(self):

        assert self.is_element_present(CartPageLocs.cart_title_loc), 'Title is not present!'
