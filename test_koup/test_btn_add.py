import time

from pages.koup_page import KoupPage
from pages.add_page import AddPage

def test_btn_add(browser):
    kp = KoupPage(browser)
    add = AddPage(browser)
    kp.visit()

    assert kp.equal_url()
    assert kp.link_add.get_text() == 'Add/Remove Elements'
    kp.link_add.click()
    time.sleep(3)
    assert add.equal_url()

    assert add.btn_add.get_text() == 'Add Element'

    assert add.btn_add.get_dom_attribute('onclick') == 'addElement()'

    for i in range(4):
        add.btn_add.click()

    assert add.delete.check_count_elements(4)

    for element in add.delete.find_elements():
        assert element.text == 'Delete'


    while add.delete.exist():
        add.delete.click()

    assert not add.delete.exist()


