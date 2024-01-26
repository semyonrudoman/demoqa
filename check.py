from pages.koup_page import KoupPage
from selenium import webdriver

driver = webdriver.Chrome()

fr = KoupPage(driver)
fr.visit()

print(fr.base_url)

text = fr.get_url()

print(text)
