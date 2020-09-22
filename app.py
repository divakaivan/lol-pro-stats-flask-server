import pandas as pd
from flask_jsonpify import jsonpify
from flask import Flask, request
import json

app = Flask(__name__)


lol_stats = pd.read_csv("./2020_LoL_esports_match_data_from_OraclesElixir_20200916.csv")


@app.route("/sample", methods=["GET"])
def hello_world():
    lol_stats_sample = lol_stats.head(10)
    lol_stats_sample = lol_stats_sample.to_json(orient="records")
    parsed = json.loads(lol_stats_sample)
    print(parsed[0])
    return json.dumps(parsed)


@app.route("/", methods=["POST"])
def get_data():
    request_info = request.get_json()
    requested_lol_stas = lol_stats.loc[lol_stats["league"] == request_info["league"]]

    requested_lol_stas = requested_lol_stas.to_json(orient="records")
    parsed = json.loads(requested_lol_stas)

    return {"data": parsed}, 200
