from pages.base_pages import BasePage
from components.components import WebElement

class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btn_under_menu = WebElement(driver, 'div:nth-child(3) > div > ul > li')
        self.icon = WebElement(driver, 'header > a > img')
        self.small_modal_btn = WebElement(driver, '#showSmallModal')
        self.modal = WebElement(driver, 'div.fade.modal.show > div > div')
        self.large_modal_btn = WebElement(driver, '#showLargeModal')
        self.large_modal_btn_close = WebElement(driver, '#closeLargeModal')
        self.small_modal_btn_close = WebElement(driver, '#closeSmallModal')
        self.modal_title = WebElement(driver, 'div.fade.modal.show > div > div > div > div')
        self.page = WebElement(driver, 'body')

