from flask import *
from datetime import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect(url_for("login"))


@app.route('/gicungdc')
def gicungdchihi():
    return "kinh kinh"


imagelist = [
    {
        "title": "vđalkjfad",
        "src": "https://static.pexels.com/photos/56875/tree-dawn-nature-bucovina-56875.jpeg"},
    {
        "title": "vđalkjf",
        "src": "https://static.pexels.com/photos/56875/tree-dawn-nature-bucovina-56875.jpeg"},
    {
        "title": "vđalkj\f",
        "src": "https://static.pexels.com/photos/56875/tree-dawn-nature-bucovina-56875.jpeg"},
    {
        "title": "vđal",
        "src": "https://static.pexels.com/photos/56875/tree-dawn-nature-bucovina-56875.jpeg"}, ]

visitor = 0


@app.route('/login')
def login():
    global visitor
    visitor += 1
    current_time_on_sever = str(datetime.now())
    return render_template("login.html", visitors=visitor * 100)


@app.route('/image')
def image():
    return render_template("imageload.html", image_list=imagelist)

@app.route('/demo')
def demo():
    return render_template("demo.html")

@app.route('/w3cssdemo')
def w3cssdemo():
    return render_template('w3cssdemo.html')
@app.route('/blogdemo')
def blogdemo():
    return render_template('blogdemo.html')

if __name__ == '__main__':
    app.run()
