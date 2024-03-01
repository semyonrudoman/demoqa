import time
from pages.alerts import AlertsPage


def test_alert(browser):
    alert = AlertsPage(browser)
    alert.visit()

    assert not alert.alert()
    alert.btn_allert.click()
    time.sleep(2)
    assert alert.alert()


def test_alert_text(browser):
    alert1 = AlertsPage(browser)
    alert1.visit()

    alert1.btn_allert.click()
    time.sleep(2)

    assert alert1.alert().text == 'You clicked a button'
    alert1.alert().accept()

    assert not alert1.alert()

def test_confirm(browser):
    confirm = AlertsPage(browser)
    confirm.visit()

    confirm.btn_confirm.click()
    time.sleep(2)
    confirm.alert().dismiss()
    assert confirm.confirm_result.get_text() == 'You selected Cancel'

def test_promt(browser):
    promt = AlertsPage(browser)
    promt.visit()
    promt.btn_promt.click()
    time.sleep(2)
    name = 'Semyon'
    promt.alert().send_keys(name)
    promt.alert().accept()
    assert promt.promt_result.get_text() == f'You entered {name}'

def test_timer_alert(browser):
    timer_alert = AlertsPage(browser)
    timer_alert.visit()

    timer_alert.btn_timer_alert.click()
    time.sleep(6)
    assert timer_alert.alert()

