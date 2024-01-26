import time
from pages.text_box_page import TextBoxPage


def test_clear(browser):
    tb = TextBoxPage(browser)
    tb.visit()

    tb.full_name.send_keys('Name')
    time.sleep(2)
    tb.full_name.clear()
    time.sleep(2)
    assert tb.full_name.get_text() == ''