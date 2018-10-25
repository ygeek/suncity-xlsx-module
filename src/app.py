import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
		return 'CONNECT SUCCESS'

@app.route('/read_xlsx', methods=['POST'])
def read_xlsx():
		xlsx_file = request.files['file']
		sheet_name = request.form['sheet_name'] or 0
		df = pd.read_excel(xlsx_file, sheet_name=sheet_name, keep_default_na=None)
		df_dict = df.to_dict('records')
		return jsonify(data=df_dict)

@app.route('/generate_template', methods=['GET'])
def generate_template():
	return '1'