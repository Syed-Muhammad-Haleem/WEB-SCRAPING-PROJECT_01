import feedparser
import json


def save_links_to_file(data,filename):

    filepath=f"all_urls/{filename}.json"

    with open(filepath,"w") as f:
        json.dump(data,f,indent=4)


def parse_rss_feed(url,name):
    links=[]
    feed=feedparser.parse(url)

    for entry in feed.entries:
        links.append(entry.link)

    data={
        "name":name,
        "urls":links
    }

    save_links_to_file(data,name)
    