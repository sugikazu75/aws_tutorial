from flask import Flask, request

app = Flask(__name__, static_folder='.', static_url_path='')
data = []

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/append', methods=['GET', 'POST'])
def append():
    if request.method == 'POST':
        data.append(request.form['message'])
    return data


app.run(port=8080, debug=True)