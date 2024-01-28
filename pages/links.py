from pages.base_pages import BasePage
from components.components import WebElement

class LinksPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/links'
        super().__init__(driver, self.base_url)

        self.link_home = WebElement(driver, 'Home', 'link')