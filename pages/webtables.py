from pages.base_pages import BasePage
from components.components import WebElement


class WebTablesPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.add_form = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.first_name_inp = WebElement(driver, '#firstName')
        self.last_name_inp = WebElement(driver, '#lastName')
        self.email_inp = WebElement(driver, '#userEmail')
        self.age_inp = WebElement(driver, '#age')
        self.salary_inp = WebElement(driver, '#salary')
        self.salary_inp = WebElement(driver, '#salary')
        self.dep_inp = WebElement(driver, '#department')
        self.btn_submit = WebElement(driver, '#submit')
        self.first_name = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(1)')
        self.last_name = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(2)')
        self.email = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(4)')
        self.age = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(3)')
        self.salary = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(5)')
        self.dep = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(6)')
        self.norows = WebElement(driver, 'div.rt-noData')
        self.btn_delete = WebElement(driver, '.action-buttons > span:nth-child(2)')
        self.btn_delete_1 = WebElement(driver, '#delete-record-4')
        self.btn_edit = WebElement(driver, '#edit-record-4')

