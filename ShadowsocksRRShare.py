#coding=utf-8
import requests
from parsel import Selector
import dateutil.parser
import time
import datetime

from tools import fromURL

class ShadowsocksRRShare:
    def start(self):
        url = "https://github.com/ruanfei/ShadowsocksRRShare/tree/master/ss"
        try:
            r = requests.get(url)
        except requests.exceptions.RequestException as e:
            print(e)
            return
        # print(r.text)
        sel = Selector(r.text)
        xList = sel.xpath("//tr[@class='js-navigation-item']")
        m = 0
        i = 0
        for index in range(len(xList)):
            c = xList[index]
            datetimeStr = c.xpath(".//@datetime").get()
            if datetimeStr == None:
                continue
            # print(datetimeStr)
            datetime = dateutil.parser.parse(datetimeStr)
            un_time = time.mktime(datetime.timetuple())
            # print(un_time)
            if un_time > m :
                m = un_time
                i = index
        href = xList[i].xpath(".//a[@class='js-navigation-open ']//@href").get()
        
            
        url2 = "https://www.github.com"+href
        print(url2)
        try:
            r2 = requests.get(url2)
        except requests.exceptions.RequestException as e:
            print(e)
            return

        sel2 = Selector(r2.text)
        href2 = sel2.xpath("//a[@id='raw-url']//@href").get()
        url3 = "https://www.github.com"+href2
        print(url3)

        try:
            r3 = requests.get(url3)
        except requests.exceptions.RequestException as e:
            print(e)
            return

        # print(r3.text)
        lineList = r3.text.split("\n")
        ret = []
        for line in lineList:
            data = fromURL(line)
            if data != None:
                ret.append(data)
        return ret

if __name__=='__main__':
    s = ShadowsocksRRShare()
    ret = s.start()
    print(ret)