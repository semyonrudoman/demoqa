from pages.base_pages import BasePage
from components.components import WebElement

class ProgressBarPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/progress-bar'
        super().__init__(driver, self.base_url)

        self.prg_bar = WebElement(driver, '#progressBar > div')
        self.start_stop_btn = WebElement(driver, '#startStopButton')
