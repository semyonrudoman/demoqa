from pages.elements import Elements

def test_find_elements(browser):
    elem = Elements(browser)

    elem.visit()

    assert elem.btns_first_menu.check_count_elements(9)
