from pages.base_pages import BasePage
from components.components import WebElement


class AddPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://the-internet.herokuapp.com/add_remove_elements/'
        super().__init__(driver, self.base_url)

        self.btn_add = WebElement(driver, '#content > div > button')
        self.delete = WebElement(driver, '#elements > button')
        # self.delete_add_1 = WebElement(driver, '#elements > button:nth-child(1)')
        # self.delete_add_2 = WebElement(driver, '#elements > button:nth-child(2)')
        # self.delete_add_3 = WebElement(driver, '#elements > button:nth-child(3)')
        # self.delete_add_4 = WebElement(driver, '#elements > button:nth-child(4)')
