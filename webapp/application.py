from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/merge', methods=['GET','POST'])
def getData():
    if request.method == 'POST':
       ## print('the data is : ',(request.data[0]))
        print((request.data))
    return 'got data'


if __name__ == "__main__":
    app.run(debug=True)