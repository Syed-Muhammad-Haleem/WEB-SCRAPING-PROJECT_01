from bs4 import BeautifulSoup
import requests
import json
import os
import threading
import PossibleArticleContentClasses




lock=threading.Lock() #

def store_article_data(name, data):

    articles=[]
    file_path = f"Extracted_Data/{name}.json"


    with lock:  # Acquire the lock before accessing the file
     
      if os.path.exists(file_path):
        
        with open(file_path, "r", encoding="utf-8") as file:
           articles = json.load(file)
      else:
         articles = []
   
       # Add new article
      articles.append(data)
   
       # Save updated data
      with open(file_path, "w", encoding="utf-8") as file:
          json.dump(articles, file, indent=4, ensure_ascii=False)


def get_content(soup):


    Article = soup.find("article")
    if Article:
        paragraphs = Article.find_all("p")
        if paragraphs:
            content1=""
            for p in paragraphs:
                content1 += p.get_text()
            
            if len(content1) > 500:
                return content1

    Main = soup.find("main")
    if Main:
        paragraphs = Main.find_all("p")
        if paragraphs:
            content2=""
            for p in paragraphs:
                content2 += p.get_text() 
            
            if len(content2) > 500:
              return content2


    

    for class_name in PossibleArticleContentClasses.Article_Classes:

        container = soup.find(class_=class_name)

        if container:

            paragraphs = container.find_all("p")

            if paragraphs:
                content3=""
                for p in paragraphs:
                    content3 += p.get_text() 

                
                if len(content3) > 500:
                    return content3

    paragraphs = soup.find_all("p")

    if paragraphs:
       content4=""
       for p in paragraphs:
            content4 += p.get_text() 
       
       if len(content4) > 500:
          return content4
       
    
    if content4=="":
        return None



def get_Value(all_data, possible_keys):

    def search(data):

        if isinstance(data, dict):
            article_type = data.get("@type")
            if isinstance(article_type, str):
                article_type = [article_type]

            is_article = False

            if article_type:
                for t in article_type:
                    if isinstance(t, str):
                        if "Article" in t or "BlogPosting" in t:
                            is_article = True
                            break

            if is_article:
                for key in possible_keys:
                    value = data.get(key)
                    if value and isinstance(value, str):
                        return value.strip()

            for value in data.values():
                result = search(value)
                if result:
                    return result

        elif isinstance(data, list):

            for item in data:
                result = search(item)
                if result:
                    return result

        return None


    for root in all_data:
        result = search(root)
        if result:
            return result

    return None





def extract(url,name):

    response = requests.get(url)
    html = response.content
    soup=BeautifulSoup(html,"html.parser")
    scripts = soup.find_all( "script",type="application/ld+json")
    all_data = []
    for script in scripts:
        try:
            data = json.loads(script.string or script.get_text())
            all_data.append(data)
        except (json.JSONDecodeError, TypeError):
            continue

    field_mapping = {

    "Title": [
        "headline",
        "name",
        "title"
    ],

    "Published_Time": [
        "datePublished",
        "dateCreated",
        "dateModified",
        "uploadDate"
    ],

    "Description": [
        "description"
    ]

}

    Title=get_Value(all_data,field_mapping["Title"])
    Description=get_Value(all_data,field_mapping["Description"])
    PublishedDate=get_Value(all_data,field_mapping["Published_Time"])
    content=get_content(soup)

    data={
            "Title":Title,
            "Published_Time":PublishedDate,
            "URL":url,
            "Description":Description,
            "Content":content
        }
    
    
    store_article_data(name,data)






