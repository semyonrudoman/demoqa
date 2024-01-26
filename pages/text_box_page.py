from pages.base_pages import BasePage
from components.components import WebElement


class TextBoxPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.full_name = WebElement(driver, '#userName')
        self.address = WebElement(driver, '#currentAddress')
        self.btn_submit = WebElement(driver, '#submit')
        self.submit_area = WebElement(driver, '#output')
        self.submit_area_name = WebElement(driver, '#name')
        self.submit_area_address = WebElement(driver, '#output > div > #currentAddress')

