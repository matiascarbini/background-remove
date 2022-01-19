from rembg.bg import remove
import numpy as np
import io
import urllib.request
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

from flask import Blueprint, jsonify, request, send_file

backgroundRemove_api = Blueprint('backgroundRemove_api', __name__)

@backgroundRemove_api.route('/background-remove', methods=["POST"])
def backgroundRemove():    
  url_image = request.json["image"]
    
  opener=urllib.request.build_opener()
  opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
  urllib.request.install_opener(opener)

  urllib.request.urlretrieve(url_image, "tmp/input.png")  
  
  input_image = 'tmp/input.png'
  output_image = 'tmp/output.png'
  f = np.fromfile(input_image)
  result = remove(f, alpha_matting=True)
  img = Image.open(io.BytesIO(result)).convert("RGBA")
  img.save(output_image)
  
  return send_file(output_image, mimetype='image/png')