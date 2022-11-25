import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

import requests
from bs4 import BeautifulSoup
url ="http://www.atmovies.com.tw/movie/next/"
Data = requests.get(url)
Data.encoding = "utf-8"
#print(Data.text)
sp = BeautifulSoup(Data.text, "html.parser")
result=sp.select(".filmListAllX li")
lastUpdate = sp.find("div", class_="smaller09").text[5:]
#print(result)
info = ""
for item in result:
	picture = item.find("img").get("src").replace(" ", "")
	title = item.find("div", class_="filmtitle").text
	movie_id = item.find("div",class_="filmtitle").find("a").get("href").replace("/","").replace("movie", "")
	hyperlink = "http://www.atmovies.com.tw" + item.find("div",class_="filmtitle").find("a").get("href")
	show = item.find("div", class_="runtime").text.replace("上映日期:","")
	show = show.replace("片長：", "")
	show = show.replace("分", "")
	showDate = show[0:15]
	showLength = show[15:]
doc = {
	"title": title,
	"picture": picture,
	"hyperlink": hyperlink,
	"showDate": showDate,
	"showLength": showLength,
	"lastUpdate": lastUpdate
}

doc_ref = db.collection("電影").document(movie_id)
doc_ref.set(doc)