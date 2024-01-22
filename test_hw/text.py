from pages.demoqa import DemoQa
from components.components import WebElement

def check_text1(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    prikol = demo_qa_page.text1.get_text()
    print(prikol)