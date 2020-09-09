from plyer import notification
import requests
from bs4 import BeautifulSoup
import time



def notifyme(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="D:\CovidNotification\icon.ico",
        timeout=10
    )

def getData(url):
       r= requests.get(url)
       return r.text


if __name__ == "__main__":
    #notifyme("Hey","Lets stop the coronavirus together")
    while true:

        myHtmlData=getData("https://www.mohfw.gov.in/")
        soup=BeautifulSoup(myHtmlData,'html.parser')
        #print(soup.prettify())
        myDataStr=""
        for tr in soup.find_all('tr').find_all('tr'):
            myDataStr+=tr.get_text()
    
        myDataStr=myDataStr[1:]
        itemList=myDataStr.split("\n\n")
        states=['Chandigarh','West Bengal','Delhi']
        for item in itemList[0:22]:
            dataList=item.split("\n")
            if dataList[1] in states:
                print(dataList)
                nTitle='Cases of Covid-19'
                nText=f"{dataList[1]}: Indian :{dataList[2]} & Foreign :{dataList[3]}\n
                Cured: {dataList[4]}\nDeaths: {dataList[5]}"
                notifyme(nTitle,nText)
                time.sleep(2)
        time.sleep(3600)

