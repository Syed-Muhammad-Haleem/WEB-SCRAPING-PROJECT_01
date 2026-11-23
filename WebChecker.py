import requests
from bs4 import BeautifulSoup

url = "https://edition.cnn.com/2026/11/23/us/chinese-spies-job-listings-national-security-invs"

response = requests.get(url, timeout=15)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

print(response.status_code)

print(soup.title.get_text(strip=True))

print(soup.get_text(" ", strip=True)[:3000])