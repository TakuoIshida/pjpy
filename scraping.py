from urllib import request
from bs4 import BeautifulSoup as bs4

def scraping():
    #url
    # url = "https://www.ncbi.nlm.nih.gov/pmc/"
    url = "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7095524/"
    # url = "https://www.nature.com/articles/s41586-020-2404-8"
    # url = "http://www.yomiuri.co.jp/"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
        }
    html = request.Request(url, headers=headers)

    response = request.urlopen(html)

    #get headlines
    # mainNewsIndex = soup.find("div", attrs={"class",  "tsec sec"})
    # title = soup.find("h1", attrs={"class",  "c-article-title"})
    # print (response.getcode())
    print (response.read())
    # title = soup.find_all("div", limit=5)
    # for res in title:
    #     print(res)
    # abst = soup.find(id="Abs1")
    # content = soup.find(id="Par1")

    #print headlines
    # for headline in headlines:
    #     print(headline.contents[0], headline.span.string)

def qiita():

    url = "https://qiita.com/U-MA/items/896c49d46585e32ff7b1"
    
    html = request.urlopen(url)

    soup = bs4(html, "html.parser")

    title = soup.find("h1", attrs={"class",  "it-Header_title"})
    print(title.string)

def nature():

    url = "https://www.natureasia.com/ja-jp/life-sci/research/13353"
    
    html = request.urlopen(url)

    soup = bs4(html, "html.parser")

    title = soup.find("h1", attrs={"class",  "title"})
    print(title.string)

if __name__ == "__main__":
    qiita()
    nature()
    scraping()
    

