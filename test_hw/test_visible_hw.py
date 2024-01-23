from pages.accordion import Accordion
import time

def test_visible_textbox(browser):
    accordion = Accordion(browser)
    accordion.visit()

    assert accordion.textbox.visible()
    assert accordion.head.visible()
    accordion.head.click()
    time.sleep(3)
    assert not accordion.textbox.visible()

def test_visible_accordion_default(browser):
    accordion = Accordion(browser)
    accordion.visit()

    assert not accordion.sec1.visible()
    assert not accordion.sec2.visible()
    assert not accordion.sec3.visible()
