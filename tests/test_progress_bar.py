import time

from pages.progress_bar import ProgressBarPage


def test_progress_bar(browser):
    pr = ProgressBarPage(browser)
    pr.visit()
    time.sleep(2)
    pr.start_stop_btn.click()

    while True:
        if pr.prg_bar.get_dom_attribute('aria-valuenow') == '51':
            pr.start_stop_btn.click()
            break

    time.sleep(2)