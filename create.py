import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc = [
{
	"title": "不可能的任務7",
	"picture": "http://www.atmovies.com.tw/photo101/fmen67015202/pl_fmen67015202_0001.jpg",
	"hyperlink": "http://www.atmovies.com.tw/movie/fmen67015202/",
	"showDate": "上映日期：2023/07/14",
	"showLength":"",
	"lastUpdate":"2022/11/18 17:19",
	"rate":"尚無電影分級資訊"
}

]

#doc_ref = db.collection("梓綸電影").document("BLwy6hAO54bO8y8Z26zT")
#doc_ref.set(doc)

collection_ref = db.collection("梓綸電影")
for doc in doc:
	collection_ref.add(doc)