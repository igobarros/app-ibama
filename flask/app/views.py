"""
Fontes:
	https://stackoverflow.com/questions/36378441/does-flask-jsonify-support-utf-8?rq=1
"""

import os
import pandas as pd

from flask import jsonify, Flask

from app import app



app.config['JSON_AS_ASCII'] = False

FILE = os.path.join(os.path.abspath('.'), 'volume')

f = os.listdir(FILE)[0]

df = pd.read_excel(FILE + '/' + f) # latitude, longitude e data_avist

@app.route('/api/v1', methods=['GET'])
def powerbi():

	columns = ['localidade', 'municipio', 'estado', 'Data_Avist', 'Latitude', 'Longitude']
	xlsx = df[columns]

	datas = []

	for x in xlsx.values:
		datas.append({
				'localidade': x[0],
				'municipio': x[1],
				'estado': x[2],
				'data_Avist': x[3],
				'latitude': str(x[4]),
				'longitude': x[5]
			})

	return jsonify({'features': datas})
