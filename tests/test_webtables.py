import time

from pages.webtables import WebTablesPage

def test_webtables(browser):
    wt = WebTablesPage(browser)

    wt.visit()
    assert not wt.norows.exist()

    while wt.btn_delete.exist():
        wt.btn_delete.click()

    time.sleep(3)
    assert wt.norows.exist()
