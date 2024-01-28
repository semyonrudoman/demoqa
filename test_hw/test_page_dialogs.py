from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa

# def test_modal_elements(browser):
#     mod_elem = ModalDialogs(browser)
#
#
#     mod_elem.visit()
#
#     assert mod_elem.btn_under_menu.check_count_elements(5)
#
# def test_navigation_modal(browser):
#     nav_mod = ModalDialogs(browser)
#     demo = DemoQa(browser)
#
#     nav_mod.visit()
#     browser.refresh()
#     nav_mod.icon.click()
#     browser.back()
#     browser.set_window_size(900, 400)
#     browser.forward()
#     assert demo.equal_url()
#     assert browser.title == 'DEMOQA'
#     browser.set_window_size(1000, 1000)

# def test_modal_dialogs(browser):
#     modal = ModalDialogs(browser)
#
#     modal.visit()
#     modal.small_modal_btn.click()
#     assert modal.modal.exist()
#     assert modal.modal_title.get_text() == 'Small Modal'
#     modal.small_modal_btn_close.click()
#     assert not modal.modal.exist()
#
#     modal.large_modal_btn.click()
#     assert modal.modal.exist()
#     assert modal.modal_title.get_text() == 'Large Modal'
#     modal.large_modal_btn_close.click()
#     assert not modal.modal.exist()

def test_modal_dialogs(browser):
    modal = ModalDialogs(browser)

    modal.visit()
    modal.small_modal_btn.click()
    assert modal.modal_title.get_text() == 'Small Modal'
    assert modal.page.visible()