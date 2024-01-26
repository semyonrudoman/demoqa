from pages.webtables import WebTablesPage


def test_input_1(browser):

    '''ПРЕДУСЛОВИЕ'''

    input = WebTablesPage(browser)

    fn = 'Semyon'
    ln = 'Rudoman'
    age = '25'
    em = 'semyonrudoman@gmail.com'
    sal = '23000'
    dep = 'QA'

    input.visit()
    input.n_of_rows.select('5 rows')

    '''ТЕСТ КЕЙС'''
    assert input.btn_next.get_dom_attribute('disabled')
    assert not input.btn_next.click()
    assert input.btn_prev.get_dom_attribute('disabled')
    assert not input.btn_prev.click()

    for i in range(3):
        input.btn_add.click()
        input.first_name_inp.send_keys(fn)
        input.last_name_inp.send_keys(ln)
        input.age_inp.send_keys(age)
        input.email_inp.send_keys(em)
        input.salary_inp.send_keys(sal)
        input.dep_inp.send_keys(dep)
        input.btn_submit.click()

    assert input.ttl_pages.get_text() == '2'
    assert not input.btn_next.get_dom_attribute('disabled')
    input.btn_next.click()
    assert input.crt_page.get_dom_attribute('value') == '2'
    input.btn_prev.click()
    assert input.crt_page.get_dom_attribute('value') == '1'


