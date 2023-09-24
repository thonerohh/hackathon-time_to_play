from flask import *
import json, time
import os
from werkzeug.utils import secure_filename
from flask import Flask
from flask_cors import CORS, cross_origin

import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import tensorflow.keras.datasets as tfds
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet_v2 import EfficientNetV2B1
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from glob import glob
import json

def predict():
    path = os.getcwd()
    prediction_folder = path + '\model\predictions'
    folder = prediction_folder + '\\*'
    files = glob(folder, recursive = True)
    model_path = path + '\model\efficientnet_40_epochs_model_1695511476.keras'#efficientnet_model.kerasefficientnet_40_epochs_model.keras
    model = tf.keras.models.load_model(model_path)
    img_height = 300
    img_width = 300
    detail_names_list = ['CS120.01.413', 'CS120.07.442', 'CS150.01.427-01', 'SU160.00.404', 'SU80.01.426', 'SU80.10.409A', 'ЗВТ86.103К-02',
    'СВМ.37.060', 'СВМ.37.060А', 'СВП-120.00.060', 'СВП120.42.020', 'СВП120.42.030', 'СК20.01.01.01.406',
    'СК20.01.01.02.402', 'СК30.01.01.02.402', 'СК30.01.01.03.403', 'СК50.01.01.404', 'СК50.02.01.411', 'СПО250.14.190']
    files = glob(folder, recursive = True)
    output_dict = {}
    if files!=[]:
        for image_path in files:
            image = tf.keras.utils.load_img(image_path)
            image = tf.image.resize(image, [img_height, img_width])
            input_arr = tf.keras.utils.img_to_array(image)
            predictions = model.predict(np.array([input_arr]))#(normalized_input_arr)
            fname = image_path[image_path.rfind('\\')+1:]
            # print('Файл ', image_path[image_path.rfind('\\')+1:], ' - Артикул: ', detail_names_list[np.argmax(predictions)])
            output_dict[fname] = detail_names_list[np.argmax(predictions)]
        return json.dumps(output_dict, indent=4, ensure_ascii=False)
    else:
        print('Проблема: Нет фотографий деталей, проверьте папку "\predictions" ')
    

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    date_set = {'Page': 'Home', 'Message': 'Successfully loaded the Home Page', 'Time': time.time()}
    return json.dumps(date_set), 200

@app.route('/request', methods=['GET'])
def request_page3():
    user_query = str(request.args.get('user'))
    data_set = {'Page': 'Request', 'Message': f'Successfully got the request {user_query}', 'Time': time.time()}
    return json.dumps(data_set), 200

@app.route('/images', methods=['POST', 'GET', 'OPTIONS'])
# @cross_origin(origin='*',headers=['Content-Type','Authorization'])
def request_page():
    files = request.files.getlist('image')
    print (request.files)
    

    # remove all files from model/predictions folder
    folder = 'model/predictions/*'
    files_in_folder = glob(folder, recursive = True)
    for f in files_in_folder:
        os.remove(f)

    image_paths = []
    for idx, file in enumerate(files):
        # save file to model/predictions folder with the same name as original
        filename = secure_filename(file.filename)
        file.save(os.path.join('model\predictions', filename))
        image_paths.append(filename)

    prediction = predict()
    return prediction, 200


@app.route('/image', methods=['POST'])
def request_page2():
    file = request.files['image']
    file.save('image_from_api.jpg')

    data_set = {'Page': 'Request', 'Message': f'Successfully got the request', 'Time': time.time()}
    return json.dumps(data_set), 200



if __name__ == '__main__':
    app.run(port=5000, debug=True)