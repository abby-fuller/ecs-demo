from flask import Flask
app = Flask(__name__)

@app.route('/api')
def hello_world():
    return ('hi!  i\'m ALSO served via Python + Flask.  i\'m a second web endpoint.')

if __name__ == '__main__':
    app.run(port='8000',host='0.0.0.0')
