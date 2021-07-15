import dload
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver')
driver.get("https://www.instagram.com/explore/tags/ootd/")
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req,'html.parser')
c =1
for i in range(1,4):
    for j in range(1,4):
        # html of the tag you want
        thumbnails = soup.select(f'#react-root > section > main > article > div.EZdmt > div > div > div:nth-child({i}) > div:nth-child({j}) > a > div > div.KL4Bh > img')
        for thumbnail in thumbnails:
            img = thumbnail['src']
            print(img)
            dload.save(img, f'img/{c}.jpg')
            c += 1

driver.quit()

