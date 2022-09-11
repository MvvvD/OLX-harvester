import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

google_forms = ''
olx_najem = ''
driver_path = ''
r = requests.get(olx_najem)
soup = BeautifulSoup(r.text, 'html.parser')
prices = soup.find_all('p', {'data-testid': 'ad-price'})
prices = [x.text.replace('złdo', 'zł do') for x in prices]
titles = soup.find_all('h6')
titles = [x.text for x in titles]
links = soup.find_all('a', {'class': 'css-1bbgabe'})
links = ['https://www.olx.pl' + x['href'] if x['href'][0] == '/' else x['href'] for x in links]
print(links)
print(titles)
print(prices)
driver = webdriver.Chrome(executable_path=driver_path)
for _ in range(len(links)):
    driver.get(google_forms)
    adres = driver.find_element(By.XPATH,
                                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    cena = driver.find_element(By.XPATH,
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH,
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    adres.send_keys(titles[_])
    cena.send_keys(prices[_])
    link.send_keys(links[_])
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
    print(_)
