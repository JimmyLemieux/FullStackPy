from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def start():
    return render_template('law/index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

while __name__ == '__main__':
    app.run(debug=True,use_reloader=False)
