from pages.base_pages import BasePage
from components.components import WebElement


class AlertsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)

        self.btn_allert = WebElement(driver, '#alertButton')
        self.btn_confirm = WebElement(driver, '#confirmButton')
        self.confirm_result = WebElement(driver, '#confirmResult')
        self.btn_promt = WebElement(driver, '#promtButton')
        self.promt_result = WebElement(driver, '#promptResult')
