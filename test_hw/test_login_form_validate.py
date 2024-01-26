from pages.form_page import FormPage


def test_login(browser):
    log = FormPage(browser)

    log.visit()
    assert log.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert log.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert log.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert log.user_email.get_dom_attribute('pattern') == r"^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"
    log.btn_submit.click_force()
    assert log.user_form.get_dom_attribute('class') == 'was-validated'
