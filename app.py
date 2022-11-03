from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    html='<button class="favorite styled" onlcick="/g" type="button">Add Airline</button>'
    return html
    
#@app.route('/add', methods=['GET', 'POST'])
