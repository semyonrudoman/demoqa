from pages.demoqa import DemoQa
from pages.elements import Elements

def test_check_text1(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    page_text1 = demo_qa_page.text1.get_text()
    if page_text1 == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.':
        assert True
    else:
        assert False

def test_check_text2(browser):
    demo_qa_page = DemoQa(browser)
    el_page = Elements(browser)

    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    page_text2 = el_page.text2.get_text()
    if page_text2 == 'Please select an item from left to start practice.':
        assert True
    else:
        assert False
