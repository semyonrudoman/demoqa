from pages.demoqa import DemoQa
from pages.accordion import Accordion
from pages.alerts import AlertsPage
from pages.browser_tab import BrowserTabPage
import pytest


@pytest.mark.parametrize('pages', [Accordion, AlertsPage, DemoQa, BrowserTabPage])
def test_seo_meta(browser, pages):
    page = pages(browser)
    page.visit()

    assert page.viewport.exist()

    assert page.viewport.get_dom_attribute('name') == 'viewport'
    assert page.viewport.get_dom_attribute('content') == 'width=device-width,initial-scale=1'
