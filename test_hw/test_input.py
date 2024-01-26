from pages.webtables import WebTablesPage


def test_input(browser):
    input = WebTablesPage(browser)

    fn = 'Semyon'
    ln = 'Rudoman'
    age = '25'
    em = 'semyonrudoman@gmail.com'
    sal = '23000'
    dep = 'QA'
    fn1 = 'Syoma'

    input.visit()
    assert input.btn_add.exist()
    input.btn_add.click()
    assert input.add_form.exist()
    input.btn_submit.click()
    assert input.add_form.exist()
    input.first_name_inp.send_keys(fn)
    input.last_name_inp.send_keys(ln)
    input.age_inp.send_keys(age)
    input.email_inp.send_keys(em)
    input.salary_inp.send_keys(sal)
    input.dep_inp.send_keys(dep)
    input.btn_submit.click()
    assert not input.add_form.exist()
    assert input.first_name.get_text() == fn
    assert input.last_name.get_text() == ln
    assert input.age.get_text() == age
    assert input.salary.get_text() == sal
    assert input.dep.get_text() == dep
    input.btn_edit.click()
    assert input.add_form.exist()
    input.first_name_inp.clear()
    input.first_name_inp.send_keys(fn1)
    input.btn_submit.click()
    assert input.first_name.get_text() == fn1
    input.btn_delete_1.click()
    assert input.first_name.get_text() == ' '
    assert input.last_name.get_text() == ' '
    assert input.age.get_text() == ' '
    assert input.salary.get_text() == ' '
    assert input.dep.get_text() == ' '


