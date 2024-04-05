from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

link_form = 'https://forms.gle/3DWn9qU4jYufikFT6'
URL_ZILLOW = 'https://appbrewery.github.io/Zillow-Clone/'

response = requests.get(URL_ZILLOW)
zillow_web_page = (response.text)
soup = BeautifulSoup(zillow_web_page, 'html.parser')

prices = soup.select(selector='ul li .PropertyCardWrapper__StyledPriceLine')
list_price = [price.getText().split('+')[0].split('/')[0] for price in prices]
# print((list_price))


links = soup.select(selector='ul li .StyledPropertyCardDataArea-anchor')
list_link = [link.get('href') for link in links]
# print(list_link)

adresses = soup.select(selector='ul li address')
list_address = [adress.getText().strip() for adress in adresses]
# print(list_address)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # keeps chrome open
driver = webdriver.Chrome(options=chrome_options)
driver.get(link_form)
for i in range(len(list_address)):
    time.sleep(1)
    address = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.send_keys(list_address[i])
    # time.sleep(1)
    
    
    price = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(list_price[i])
    # time.sleep(1)
    
    link = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(list_link[i])
    # time.sleep(1)
    
    enviar = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    enviar.click()
    time.sleep(1)
    
    another_ans = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_ans.click()

driver.quit()
    