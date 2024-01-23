from pages.base_pages import BasePage
from components.components import WebElement

class Accordion(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.textbox = WebElement(driver, '#section1Content > p')
        self.head = WebElement(driver, '#section1Heading')
        self.sec1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.sec2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.sec3 = WebElement(driver, '#section3Content > p')