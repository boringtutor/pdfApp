from flask import Flask,render_template,request,jsonify
import requests
import pyrebase
import sys
import urllib
import app2 as ap

config = {
    "apiKey": "AIzaSyByGXa1C7S-X_kxkJqHP3ShNKwnF5caYic",
    "authDomain": "pdf-github.firebaseapp.com",
    "databaseURL": "https://pdf-github.firebaseio.com",
    "projectId": "pdf-github",
    "storageBucket": "pdf-github.appspot.com",
    "messagingSenderId": "582888951051"
}



firebase = pyrebase.initialize_app(config)

# Get a reference to the database service
db = firebase.database()


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')
@app.route('/merge')
def mergeTheFile():
    print('calling the merging...')
    merge()
    return jsonify({'d':'done'})

def merge():
    data = db.child('pdfs').get()
    urls = []
    keys= []
    for val in data.val():
        if val is not None:
            for key in val.keys():
                urls.append(val[key])
    
    #my_url = str(urls[0])
    ur=[]
    i=2

    for url in urls:
        if i%2 == 0:
            ur.append(url)
        i=i+1
    dirs = []
    for u in ur:
        try:
            print('loading')
            loader = urllib.request.urlretrieve(u,'./*.pdf')
            
        except urllib.error.URLError as e:
            message = json.loads(e.read())
            print(message["error"]["message"])
        else:
            print('the loader is : ')
            print((loader[0]))
            dirs.append(loader[0])
            #ap.test()
    print('directories are :')
    ap.test(dirs)

if __name__ == "__main__":
    app.run(debug=True)