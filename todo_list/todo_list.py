from flask import Flask, request, render_template

app = Flask(__name__, static_folder='.', static_url_path='')
data = []
checked_list = []

@app.route('/')
def index():
    # return app.send_static_file('templates/index.html')
    return render_template('index.html', todo_list=data, checked_list=checked_list)

@app.route('/append', methods=['GET', 'POST'])
def append():
    if request.method == 'POST':
        data.append(request.form['message'])
    return render_template('index.html', todo_list=data, checked_list=checked_list)

@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        if(request.form['message'] in data):
            data.remove(request.form['message'])
    return render_template('index.html', todo_list=data, checked_list=checked_list)
  
@app.route('/reset', methods=['GET'])
def reset():
    global data, checked_list
    data = []
    checked_list = []
    return render_template('index.html', todo_list=data, checked_list=checked_list)

@app.route('/update', methods=['POST'])
def add():
    global checked_list
    checked_list = request.form.getlist('todo_checkbox')
    # print(checked_list)
    return render_template('index.html', todo_list=data, checked_list=checked_list)
 
app.run(port=8080, debug=True)