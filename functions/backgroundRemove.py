from rembg.bg import remove
import numpy as np
import io
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

from flask import Blueprint, jsonify, request, send_file

backgroundRemove_api = Blueprint('backgroundRemove_api', __name__)

@backgroundRemove_api.route('/background-remove', methods=["POST"])
def backgroundRemove():    
  url_image = request.json["image"]
  
  import urllib
  urllib.request.urlretrieve(url_image, "tmp/input.png")
  
  input_image = 'tmp/input.png'
  output_image = 'tmp/output.png'
  f = np.fromfile(input_image)
  result = remove(f, alpha_matting=True)
  img = Image.open(io.BytesIO(result)).convert("RGBA")
  img.save(output_image)
  
  return send_file(output_image, mimetype='image/png')