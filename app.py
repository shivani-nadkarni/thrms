from flask import Flask, render_template, request

app = Flask(__name__)
l = list()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html', items = l)
    if request.method == 'POST':
        tmp = request.form['descr']
        l.append(tmp)
        return render_template('home.html', items = l)
    
    
if __name__ == '__main__':
    app.run(debug=True)
