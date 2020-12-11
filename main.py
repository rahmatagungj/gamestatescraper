import os
import time
import requests
import pyfiglet as draw
from tqdm import tqdm 
from bs4 import BeautifulSoup

to_show = ['Hostname','Players','Mapname'] 

def players(self,data):
    os.system("cls")
    
def UI():
    os.system("cls")
    os.system("color a")
    os.system("title Game State Scraper - by Rahmat Agung Julians")
    banner = draw.figlet_format("Game State Scrapper!!")
    print(banner)
    
def loading():
    for _ in tqdm(range(100), desc="GETTING INFORMATION", ascii=False,ncols=75):
        time.sleep(0.05)
    os.system("cls")
    
class scrap(object):
    def __init__(self,search):
        self.search = search 

    def __repr__(self):
        status = self.process()
        os.system("pause")
        return str(f"Its is {status} for {self.search}") 
    
    def process(self):
        url = f"https://www.game-state.com/index.php?search={self.search}"
        req = requests.get(url)
        scrape = BeautifulSoup(req.text, "html.parser")
        element = scrape.find_all('div', class_='contents',style="min-height: 400px;")
        for elm in element:
            contents = elm.find('tr', class_='even')
            if contents is None:
                return 'fail'
            for show in to_show:
                toBeShow = contents.find('td', class_=show.lower())
                if toBeShow is not None:
                    toBeShow = toBeShow.get_text()
                else:
                    toBeShow = None
                print(show,"\t: ", toBeShow, end='\n'*2)
        return 'done'

if __name__ == "__main__":
    UI()
    to_find = str(input("Enter Server Name : "))
    loading()
    print(scrap(to_find))
    
#Republic City