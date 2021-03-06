import requests
import sys, threading
from bs4 import BeautifulSoup, SoupStrainer
import lxml

discountPrice =[]
medication ="xanax"
store =[]
distance =""
url_idc=""
url_goodRx = "https://www.goodrx.com/"

def crawl_goodRx(medication):

    print("Calling crawl_goodRx")

    global originalPrice
    global discountPrice
    global store
    global url
    global keys

    url = url_goodRx + medication + "?drug-name=" + medication
    sourceCode = requests.get(url)
    plainText = sourceCode.text
    strainer = SoupStrainer('div', {'class': 'store-name '})
    name_soup = BeautifulSoup(plainText, "lxml", parse_only=strainer)
    strainer2 = SoupStrainer('div', {'class': 'pricerow-drugprice'})
    number_soup = BeautifulSoup(plainText, "lxml", parse_only=strainer2)

    for x in name_soup.find_all(class_ ='store-name'):
        store.append(x.text.strip())
    for x in number_soup.find_all(class_ ='drug-price'):
        discountPrice.append(float(x.text.strip('$')))

    dict_ = {}
    for s_name, dPrice in zip(store, discountPrice):
        dict_[s_name] = dPrice

    for x in dict_:
        print ("{} {}".format(x, dict_[x]))
    return dict_

def crawl_idc():
    url_idc = "https://www.internetdrugcoupons.com/" + medication + "-coupon"
    sourceCode = requests.get(url_idc)
    plainText = sourceCode.text
    strainer = SoupStrainer('div', {'class': 'my-coupon'})



if __name__ == "__main__":
    #goodrx = crawl_goodRx()
    idc = crawl_idc()
