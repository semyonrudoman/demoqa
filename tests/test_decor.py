from pages.demoqa import DemoQa
from pages.radio_button import RadioButton
import pytest

@pytest.mark.skip
def test_decor(browser):
    decor = DemoQa(browser)
    decor.visit()
    assert decor.title.check_count_elements(6)
    for element in decor.title.find_elements():
        assert element.text != ''

@pytest.mark.skipif(True, reason='просто пропуск')
def test_radio(browser):
    rad = RadioButton(browser)
    rad.visit()
    rad.btn_yes.click_force()
    assert rad.text.get_text() == 'You have selected Yes'
    rad.btn_imp.click_force()
    assert rad.text.get_text() == 'You have selected Impressive'
    assert 'disabled' in rad.btn_no.get_dom_attribute('class')