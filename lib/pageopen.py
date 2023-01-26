from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_soup_from_sel(URL):
    driver = webdriver.Chrome()
    driver.get(URL)
    return BeautifulSoup(driver.page_source, "html.parser")

# print(get_soup_from_sel("https://www.secrettelaviv.com/tickets/bad-night-sponsored-by-a"))