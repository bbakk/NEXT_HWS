from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

# 디버깅 모드
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

#내 chrome.exe있는 위치는 C:\Program Files\Google\Chrome\Application\chrome.exe
#powershell에서 해당 위치로 들어가서 .\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTEMP” 를 치면 chrome 페이지가 열림
#그리고 파이썬 런하면 됩니다요

chrome_driver = './chromedriver.exe'
driver = webdriver.Chrome(chrome_driver, options= chrome_options)

# 실행할 웹페이지 불러오기 (네이버무비)
driver.get("https://movie.naver.com/")
time.sleep(1)

#csv열기
file = open('movie.csv', mode='w', newline='')
writer= csv.writer(file)
writer.writerow(["number", "title", "outline", "director", "rating"])

# 네이버영화랭킹 클릭하기
chartbtn = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
chartbtn.click()
time.sleep(1)

#네이버영화 1위부터 20위까지 가져오기
for i in range(1,21):
    if i<= 10:
        titles = driver.find_element(By.XPATH,f"/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i+1}]/td[2]/div/a").text
    else:
        titles = driver.find_element(By.XPATH,f"/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i+2}]/td[2]/div/a").text
    print(i, titles)
    time.sleep(1)

# 1위부터 20위까지 클릭해서 파일에 저장(beautifulsoup 활용)
# source = driver.page_source
# soup = BeautifulSoup(source, 'html.parser')

# 1위부터 20위까지 클릭해서 파일에 저장
# 자꾸 막히는게 있어서 try except 쓸수 밖에 없었음
for i in range(20):
    if i<10:
            rank = driver.find_element(By.XPATH, f'//*[@id="old_content"]/table/tbody/tr[{i+2}]/td[2]/div/a')
    else:
            rank = driver.find_element(By.XPATH, f"/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i+3}]/td[2]/div/a")
    try:
        rank.click()
        number = i+1
        title = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[1]/h3/a[1]').text
        outline = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]').text
        director = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
        rating = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]/div/div/em').text
        writer.writerow([number, title, outline, director, rating])
        time.sleep(1)
        driver.back()
    except:
         rating = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[4]/div[2]/div[2]/div[1]/div/div/em').text
         writer.writerow([number, title, outline, director, rating])
         time.sleep(1)
         driver.back()
file.close()

# 좋아하는 영화 콘텐츠 검색하기
file = open('myfav.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["title", "outline", "director", "rating",])

search = driver.find_element(By.XPATH, '//*[@id="ipt_tx_srch"]')
search.send_keys("코렐라인")
search.send_keys(Keys.ENTER)
time.sleep(1)

fav = driver.find_element(By.XPATH, '//*[@id="old_content"]/ul[2]/li/p/a/img')
fav.click()
title = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[1]/h3/a[1]').text
outline = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]').text
director = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
rating = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]/div/div/em').text
writer.writerow([title, outline, director, rating])