from pages.base_pages import BasePage
from components.components import WebElement


class KoupPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://the-internet.herokuapp.com/'
        super().__init__(driver, self.base_url)

        self.link_add = WebElement(driver, '#content > ul > li:nth-child(2) > a')