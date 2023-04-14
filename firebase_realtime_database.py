import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyBaWELhVWlVo33ua2ojk0M-CxgB87c8su0",
    'authDomain': "streamlit-course-gs.firebaseapp.com",
    'projectId': "streamlit-course-gs",
    'storageBucket': "streamlit-course-gs.appspot.com",
    'messagingSenderId': "294729790189",
    'appId': "1:294729790189:web:2c5867eed2198689abd2e4",
    'databaseURL': 'https://streamlit-course-gs-default-rtdb.firebaseio.com/'
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

data= {'ks21040277': {
        'name': '김성채',
        "age" : 18,
        "adress" : '대구 북구'
}}
# print(db.push(data))
db.child("users").push(data)

data2= {'ks2104027': {
        'name': '김성',
        "age" : 8,
        "adress" : '대구 구'
}}
# print(db.push(data))
db.child("users").push(data2)