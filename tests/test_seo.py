from pages.demoqa import DemoQa


def test_check_title(browser):
    demoqa = DemoQa(browser)

    demoqa.visit()
    assert browser.title == 'DEMOQA'