from urllib import request
from bs4 import BeautifulSoup

def scraping():
    #url
    url = "https://www.ncbi.nlm.nih.gov/pmc/"
    # url = "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7095524/"
    # url = "http://www.yomiuri.co.jp/"
    # url = "http://www.yomiuri.co.jp/"

    html = request.urlopen(url)

    soup = BeautifulSoup(html, "html.parser")

    #get headlines
    # mainNewsIndex = soup.find("div", attrs={"class",  "tsec sec"})
    title = soup.find("div", attrs={"class",  "headerimage"})
    # abst = soup.find(id="Abs1")
    # content = soup.find(id="Par1")

    #print headlines
    # for headline in headlines:
    #     print(headline.contents[0], headline.span.string)
    print(title)
    print(title.string)

def qiita():

    url = "https://qiita.com/U-MA/items/896c49d46585e32ff7b1"
    
    html = request.urlopen(url)

    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("h1", attrs={"class",  "it-Header_title"})
    print(title.string)

def nature():

    url = "https://www.natureasia.com/ja-jp/life-sci/research/13353"
    
    html = request.urlopen(url)

    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("h1", attrs={"class",  "title"})
    print(title.string)

if __name__ == "__main__":
    qiita()
    nature()
    scraping()
    

