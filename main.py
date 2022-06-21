from urllib import response
import requests , json,time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
loc_dt = datetime.datetime.today() 
num_=["001","005"]
data=[]
for i in num_:
        url="https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-{}?Authorization=CWB-D98DF98F-D9C4-4B7F-8A3D-D615CB11BE84".format(i)
        r=requests.get(url).json()
        data.append(r)

cred = credentials.Certificate('firebasekey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
for obj in data:
    doc_ref = db.collection(str(loc_dt.strftime("%Y/%m/%d %H:%M"))).document(obj["records"]["locations"][0]["locationsName"])
    doc_ref.set({"縣市":obj["records"]["locations"][0]["locationsName"]})
    for obj_ in obj["records"]["locations"][0]["location"]:
        doc_ref.update(({obj_["locationName"]:obj_["weatherElement"]}))
    


