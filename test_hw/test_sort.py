from pages.webtables import WebTablesPage


def test_sort(browser):
    sort_table = WebTablesPage(browser)
    sort_table.visit()
    sort_table.first_name_title.click()
    assert sort_table.table_body.sorted()



