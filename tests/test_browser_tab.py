import time
from pages.links import LinksPage
#
#
# def test_browser_tab(browser):
#     browser_tab = BrowserTabPage(browser)
#     browser_tab.visit()
#
#     assert len(browser.window_handles) == 1
#
#     browser_tab.new_tab.click()
#     time.sleep(2)
#     assert len(browser.window_handles) == 2
#     browser.switch_to.window(browser.window_handles[0])
#     time.sleep(2)

def test_window_tab(browser):
    link = LinksPage(browser)
    link.visit()

    assert link.link_home.get_text() == 'Home'
    assert link.link_home.get_dom_attribute('href') == 'https://demoqa.com'
    link.link_home.click()
    assert len(browser.window_handles) == 2
