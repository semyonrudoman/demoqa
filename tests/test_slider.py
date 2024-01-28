from pages.slider import SliderPage
from selenium.webdriver.common.keys import Keys


def test_slider(browser):
    sl = SliderPage(browser)
    sl.visit()

    assert sl.slider.exist()
    assert sl.slider_text.exist()

    while not sl.slider_text.get_dom_attribute('value') == '50':
        sl.slider.send_keys(Keys.ARROW_RIGHT)

    assert sl.slider_text.get_dom_attribute('value') == '50'
