from flask import Flask
from functions.backgroundRemove import backgroundRemove_api

app = Flask(__name__)

app.register_blueprint(backgroundRemove_api)

@app.route('/')
def getInit():  
  return 'Estoy vivo'

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=5000)