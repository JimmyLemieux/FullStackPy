from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def start():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/')

while __name__ == '__main__':
    app.run(debug=True,use_reloader=False)
