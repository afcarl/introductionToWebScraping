import requests
import lxml.html

base_url = "https://www.google.com"

def scrape(url,base_url,depth):
    if depth == 0:
        return True
    r = requests.get(url)
    html = lxml.html.fromstring(r.text)
    links = html.xpath("//a/@href")
    for ind,link in enumerate(links):
        if "http" in link:
            print link
        else:
            print base_url+link
            links[ind] = base_url+link
    for link in links:
        scrape(link,base_url,depth-1)

scrape(base_url,base_url,5)
