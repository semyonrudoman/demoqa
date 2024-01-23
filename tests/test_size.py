import time

from pages.demoqa import DemoQa


def test_check_title(browser):
    demoqa = DemoQa(browser)

    demoqa.visit()

    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(1000, 1000)