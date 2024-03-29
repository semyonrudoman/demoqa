from pages.demoqa import DemoQa
from pages.accordion import Accordion
from pages.alerts import AlertsPage
from pages.browser_tab import BrowserTabPage
import pytest
import time

@pytest.mark.parametrize('pages', [Accordion, AlertsPage, DemoQa, BrowserTabPage])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)

    page.visit()
    time.sleep(2)
    assert page.get_title() == 'DEMOQA'




# def test_check_title(browser):
#     demoqa = DemoQa(browser)
#
#     demoqa.visit()
#     assert browser.title == 'DEMOQA'