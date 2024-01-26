from pages.text_box_page import TextBoxPage


def test_text_box(browser):
    tb = TextBoxPage(browser)
    name = 'Tester Testerov'
    address = 'Test st'

    tb.visit()
    tb.full_name.send_keys(name)
    tb.address.send_keys(address)
    tb.btn_submit.click_force()
    assert tb.submit_area.visible()
    assert tb.submit_area_name.get_text() == 'Name:' + name
    assert tb.submit_area_address.get_text() == 'Current Address :' + address
