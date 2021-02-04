from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/popup.html')
def popup_page():
    return render_template('popup.html')

if __name__ == '__main__':
    app.run()