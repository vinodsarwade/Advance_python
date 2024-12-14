'''
Real- World example: Multithreading for i/o bound tasks.
Scenario : Web Scraping

web scrapping often involves making numerous network request to
fetch web page. this task are I/O bound task bcz they spend a lot of time
waiting for responces from server.Multithreading can significantly improve
the performance by allowing multiple web pages to be fetched concurrently.

'''
import threading 
import requests
from bs4 import BeautifulSoup

urls = [
    'https://www.langchain.com/',
    'https://pandas.pydata.org/',
    'https://python.langchain.com/docs/introduction/'
]

def fetch_data(url):
    responce = requests.get(url)
    soup = BeautifulSoup(responce.content,'html.parser')
    print(f"Fetched {len(soup.text)} characters from{url}")

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_data,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched")
