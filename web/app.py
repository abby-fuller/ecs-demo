from flask import Flask
app = Flask(__name__)

@app.route('/web')
def hello_world():
    return ('hi!  i\'m served via Python + Flask.  i\'m a web endpoint.')

if __name__ == '__main__':
    app.run(port='3000',host='0.0.0.0')
