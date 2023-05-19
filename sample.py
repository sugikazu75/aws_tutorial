from flask import Flask
app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return '<html><body><h1>Flask framework!</h1></body></html>'

app.run(port=8080, debug=True)