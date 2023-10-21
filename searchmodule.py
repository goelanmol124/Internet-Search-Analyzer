from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import random

def rtime(a,b):
    return time.sleep(random.randint(a*100,b*100)/100)
def getqueryfile(query,filename):
    retries = 2
    requests.adapters.DEFAULT_RETRIES = retries
    driver = webdriver.Chrome(executable_path=r"C:\Users\goela\Development\chromedriver.exe")
    rtime(1,2)
    fil = filename
    with open(fil, 'w') as f:
        f.write("----start----")
        f.write("Query = "+query)
        
    driver.get("https://www.bing.com/search?q={}".format(query))
    rtime(2,4)
    search_results = driver.find_elements_by_tag_name('cite')
    res = []
    for search_result in search_results:
        search_result = search_result.text
        res.append(search_result)
        with open(fil, 'a') as f:
            f.write('')
            f.write("relevant Websites")
            f.write('')
            f.write(search_result)
    count = 0
    for url in res:
        print('---------------------------')
        count += 1
        print(url)
        print(count ,'/',len(res))
        try:
            rtime(1,2)
            if url[0:4] != 'http':
                url = 'https://' + url
            driver.get(url)
            rtime(3,6)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            soup = soup.find('body')
            try:
                unwanted = soup.find('footer')
                unwanted.extract()
            except:
                pass
            paragraphs = soup.find_all('p')
            list_items = soup.find_all('li')
            with open(fil,'a+', encoding="utf-8") as f:
                for i in paragraphs:
                    f.write(i.get_text().strip())
                for i in list_items:
                    f.write(i.get_text().strip())
                f.write('')
        except Exception as E:
            print(E)
    driver.quit()

getqueryfile("Best Destinations in Delhi for photowalks",r"C:\Users\goela\Development\Python\myfile.txt")