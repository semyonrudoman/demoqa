from pages.text_box_page import TextBoxPage

def test_text_box_submit(browser):
    tb = TextBoxPage(browser)
    tb.visit()

    assert tb.btn_submit.check_css('color', 'rgba(255, 255, 255, 1)')
    assert tb.btn_submit.check_css('backgroundColor', 'rgba(0, 123, 255, 1)')
    assert tb.btn_submit.check_css('borderColor', 'rgb(0, 123, 255)')
