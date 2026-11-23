from bs4 import BeautifulSoup
import requests
import json


def save_data_to_file(Links,name):

    filepath=f"all_urls/{name}.json"

    with open(filepath,"r") as f:
        data=json.load(f)

    data["urls"]=list(set(data["urls"]+Links))  # this will remove the duplicate links through rss and sitemap

    with open(filepath,"w") as f:
        json.dump(data,f,indent=4)



def parse_sitemap(url,name):

    response=requests.get(url)
    soup=BeautifulSoup(response.content,"xml")
    Links=[]

    Links_TAG_Container=soup.find_all("loc")
      
    for linkTAG in Links_TAG_Container:
        Links.append(linkTAG.get_text(strip=True))

    save_data_to_file(Links,name)

