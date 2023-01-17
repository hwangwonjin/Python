"""
날짜 : 2023/01/17
이름 : 황원진
내용 : 파이썬 기상청 날씨 크롤링 실습하기
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pymysql


# 가상 브라우저 실행
chrome_oprions = Options()
chrome_oprions.add_experimental_option("detach", True)

browser = webdriver.Chrome('./chromedriver.exe', options=chrome_oprions)

# 페이지 이동
browser.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')

# 지역명 출력
trs = browser.find_elements(By.CSS_SELECTOR, '#weather_table > tbody > tr')


for tr in trs:
    tds = tr.find_elements(By.CSS_SELECTOR, 'td')
    print('지역명 : ', tds[0].text)

# 가상 브라우저 종료
browser.close()

