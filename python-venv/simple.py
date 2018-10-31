#export FLASK_APP=simple.py 
#^ to import
#flask run --host=0.0.0.0   
#^ to execute.

from flask import Flask

app = Flask(__name__)
#apparently name is none for some reason?
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
@app.route('/')
def hello():
    return "<h1> Hello Everyone! </h1>" 
