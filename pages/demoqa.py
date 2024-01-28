from pages.base_pages import BasePage
from components.components import WebElement
class DemoQa(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        self.text1 = WebElement(driver, '#app > footer > span')
        self.title = WebElement(driver, 'div.card-body > h5')

