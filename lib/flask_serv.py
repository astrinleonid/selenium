import numpy as np
import pandas as pd
import pickle
import json
# from IPython.display import display
from sklearn.neighbors import KNeighborsClassifier
from flask import Flask
from flask import request
from flask import jsonify
from db_class import StorageDatabase

FEATURES = ['is_male','num_inters','late_on_payment','age','years_in_contract']
# Reading datafiles
with open('churn_model.pkl', 'rb') as file:
    clf = pickle.load(file)

features = FEATURES

app = Flask(__name__)

# Individual prediction
@app.route("/get_event")
def get_event():
    event_id = request.args.get("event_id")
    city = request.args.get("city")
    # db.table_get_value_with_ID(self, table, event_id, columns)
    data = {
        "Header": "Sample Event Header",
        "Description": "Sample Event Description",
        "Date": "Sample Event Date",
        "Genre": "Sample Event Genre",
        "Price": "Sample Event Price",
        "Location": "Sample Event Location",
    }
    print(f"recived: event_id={event_id}")
    data = [1,2,3,4]
    return jsonify(data)

#Bulk prediction


app.run(host='0.0.0.0', port=8080)

from flask_serv import Flask, jsonify, request

app = Flask("ds_stub")


@app.route("/get_event")
def get_event():
    event_id = request.args.get("event_id")
    target_city = request.args.get("target_city")

    data = {
        "Header": "Sample Event Header",
        "Description": "Sample Event Description",
        "Date": "Sample Event Date",
        "Genre": "Sample Event Genre",
        "Price": "Sample Event Price",
        "Location": "Sample Event Location",
    }
    print(f'recived: event_id={event_id}, target_city={target_city}')
    return jsonify(data)


if __name__ == "__main__":
    app.run()









