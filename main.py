from flask import Flask
from functions.backgroundRemove import backgroundRemove_api

import os
if os.path.exists('./tmp') == False:
  os.mkdir("./tmp")

app = Flask(__name__)

app.register_blueprint(backgroundRemove_api)

@app.route('/')
def getInit():  
  return 'ELIMINAR FONDO DE IMÁENES'

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=False, port=5000)