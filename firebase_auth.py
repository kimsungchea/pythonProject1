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

firebase = pyrebase.initialize_app((firebaseConfig))
auth = firebase.auth()

# auth.create_user_with_email_and_password('ks21940277@gmail.com', 'k@0536223883')
isLogged = False

try:

    login = auth.sign_in_with_email_and_password('ks21940277@gmail.com', 'k@0536223883')
    user = auth.get_account_info(login['idToken'])
    # print(user['users'][0]['localId'])
    print(user)

    isLogged = True


except Exception as e:
    print(e)

if isLogged == True:
    print('로그인 성공')
else:
    print('로그인 실패')