from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    try:
        return render_template('index.html', hostname='test', ip='123.123.123.123')
    except:
        return render_template('error.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=40204)
