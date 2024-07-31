from flask import Flask, request, jsonify
from flask import Flask, request, jsonify, send_from_directory

import  util
import os
app = Flask(__name__)
def initialize():
    util.load_saved_artifacts()

@app.route('/')
def index():
   return send_from_directory('static', 'app.html')

@app.route('/get_location_names', methods=['GET'])
def get_location_name():
    response = jsonify({
        'locations': util.get_location_name()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# @app.route('/get_location_name')
# def get_location_name():
#     # initialize()
#     response =jsonify({
#         'locations':util.get_location_name()
#     })
#     response.headers.add('Access-Control-Allow-Origin','*')
#     return  response

# @app.route('/predict_home_price',methods=['POST'])
@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    print(total_sqft)
    print(location)
    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
        # 'estimated_price': util.get_estimated_price('1st phase jp nagar', 1000, 2, 2)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# def predict_home_price():
#     total_sqft=float(request.form['total_sqft'])
#     location=request.form['location']
#     bhk=int(request.form['bhk'])
#     bath=int(request.form['bash'])
#     response = jsonify({
#         'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
#     })
#     return  response
if __name__ == "__main__":
    # print("Starting python flask server!")
    # initialize()
    # # print(util.get_location_name())
    # # print(util.get_estimated_price('1st phase jp nagar', 1000, 2, 2))
    # app.run()
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting python flask server on port {port}!")
    initialize()
    app.run(host='0.0.0.0', port=port)
