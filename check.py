from pages.koup_page import KoupPage
from selenium import webdriver
from pages.alerts import AlertsPage
import time

driver = webdriver.Chrome()

fr = KoupPage(driver)
fr.visit()

print(fr.base_url)

text = fr.get_url()

print(text)


alert = AlertsPage(driver)
alert.visit()

alert.btn_allert.click()
time.sleep(2)

print(alert.alert().text)
