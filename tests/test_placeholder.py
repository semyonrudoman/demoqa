import time
from pages.text_box_page import TextBoxPage


def test_placeholder(browser):
    ph = TextBoxPage(browser)

    ph.visit()
    assert ph.full_name.get_dom_attribute('placeholder') == 'Full Name'
