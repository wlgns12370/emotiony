import dload
from bs4 import BeautifulSoup
from selenium import webdriver
import time
driver = webdriver.Chrome('chromedriver')


driver.get("https://www.instagram.com/explore/tags/ootd/")
time.sleep(3)

req = driver.page_source
soup = BeautifulSoup(req,'html.parser')

thumbnails = soup.select('#react-root > section > main > article > div.EZdmt > div > div > div:nth-child(1) > div:nth-child(1) > a > div > div.KL4Bh > img')

i = 1
for thumbnail in thumbnails:
    img = thumbnail['src']
    dload.save(img, f'img/{i}.jpg')
    i += 1


driver.quit()

