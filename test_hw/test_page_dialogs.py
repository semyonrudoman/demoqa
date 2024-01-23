from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa

def test_modal_elements(browser):
    mod_elem = ModalDialogs(browser)


    mod_elem.visit()

    assert mod_elem.btn_under_menu.check_count_elements(5)

def test_navigation_modal(browser):
    nav_mod = ModalDialogs(browser)
    demo = DemoQa(browser)

    nav_mod.visit()
    browser.refresh()
    nav_mod.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert demo.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)

