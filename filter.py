from Filter_system.url_filter import filter_url
import json

def filter_all_urls(name):

    filepath=f"all_urls/{name}.json"

    with open(filepath,"r") as f:
        data=json.load(f)


    Filtered_urls=[]

    for url in data["urls"]:
        is_True1=filter_url(url)
       
        if is_True1:
             Filtered_urls.append(url)

    data={
        "name":name,
        "urls":Filtered_urls
    }
            
    filepath2=f"Filtered_urls/{name}.json"  
    
    with open(filepath2,"w") as file:
        json.dump(data,file,indent=4)
    