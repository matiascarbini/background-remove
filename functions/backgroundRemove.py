from rembg.bg import remove
import numpy as np
import io
import string
import random
import urllib.request
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

from flask import Blueprint, jsonify, request, send_file, send_from_directory

backgroundRemove_api = Blueprint('backgroundRemove_api', __name__)

@backgroundRemove_api.route('/background-remove', methods=["POST"])
def backgroundRemove():    
  url_image = request.json["image"]
    
  opener=urllib.request.build_opener()
  opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
  urllib.request.install_opener(opener)

  strRandom = ''
  number_of_strings = 5
  length_of_string = 8
  for x in range(number_of_strings):
    strRandom = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))

  input_image = 'tmp/input_' + strRandom + '.png'
  urllib.request.urlretrieve(url_image, input_image)  
    
  f = np.fromfile(input_image)
  result = remove(f, alpha_matting=True)
  img = Image.open(io.BytesIO(result)).convert("RGBA")
  
  output_image = 'output_' + strRandom + '.png'
  img.save(output_image)
      
  return request.host_url + 'image/' + output_image  
  #return send_file(output_image, mimetype='image/png')
  
@backgroundRemove_api.route('/image/<path:filename>')
def protected(filename):    
	return send_from_directory('tmp',filename)