from pages.demoqa import DemoQa
from pages.elements import Elements

def test_navgation(browser):
    demoqa_page = DemoQa(browser)
    el_page = Elements(browser)

    demoqa_page.visit()
    demoqa_page.btn_elements.click()
    el_page.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    assert el_page.equal_url()
