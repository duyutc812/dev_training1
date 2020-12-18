from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests


# Cách 1
url = 'http://45.79.43.178/source_carts/wordpress/wp-login.php'
s = requests.Session()
data = {
    'log': 'admin',
    'pwd': '123456aA'
    # name
}
res = s.post('http://45.79.43.178/source_carts/wordpress/wp-login.php', data=data)
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
print('Username:', soup.find('span', class_='display-name').get_text())


# # Cách 2
# driver = None
#
# cpath = "E:\\chromedriver.exe"
# driver = webdriver.Chrome(cpath)
# driver.get("http://45.79.43.178/source_carts/wordpress/wp-login.php")
# e = driver.find_element(By.ID, "user_login")
# e.send_keys("admin")
# e = driver.find_element(By.ID, "user_pass")
# e.send_keys("123456aA")
# e = driver.find_element(By.ID, 'wp-submit')
# e.click()
#
# # print(driver.page_source.find_all('display_name'))
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# print('Username:', soup.find('span', class_='display-name').get_text())



