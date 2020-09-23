import pandas as pd
from flask_jsonpify import jsonpify
from flask import Flask, request
import json

app = Flask(__name__)


lol_stats = pd.read_csv("./lol_pro_stats_2020.csv")


@app.route("/sample", methods=["GET"])
def hello_world():
    lol_stats_sample = lol_stats.head(10)
    lol_stats_sample = lol_stats_sample.to_json(orient="records")
    parsed = json.loads(lol_stats_sample)

    return json.dumps(parsed)


@app.route("/", methods=["POST"])
def get_data():
    request_info = request.get_json()
    requested_lol_stats = lol_stats
    supported_leagues = ["LCK", "LEC", "LCS", "LPL"]
    if "league" in request_info:
        if request_info["league"] not in supported_leagues:
            return {
                "data": {
                    "error": "The league you are trying to access is not yet supported. Available leagues: {0}".format(
                        supported_leagues
                    )
                }
            }

        requested_lol_stats = requested_lol_stats.loc[
            (requested_lol_stats["league"] == request_info["league"])
            & (requested_lol_stats["position"] == "team")
        ]

    if "amount" in request_info:
        requested_lol_stats = requested_lol_stats.head(request_info["amount"])

    if "split" in request_info:
        if request_info["split"].lower() not in ["spring", "summer"]:
            return {"data": {"error": "Split must be either spring or summer"}}, 500

        requested_lol_stats = requested_lol_stats[
            requested_lol_stats["split"] == request_info["split"]
        ]

    if "patch" in request_info:

        available_patches = requested_lol_stats["patch"].unique()
        if request_info["patch"] not in available_patches:
            return {
                "data": {
                    "error": "The patch by which you filter is either unavailable or incorrect. Available patches are: {0}".format(
                        available_patches
                    )
                }
            }, 500

        requested_lol_stats = requested_lol_stats[
            requested_lol_stats["patch"] == request_info["patch"]
        ]

    if "team" in request_info:
        requested_lol_stats["team"] = requested_lol_stats["team"].str.upper()
        available_teams = requested_lol_stats["team"].unique()
        if request_info["team"].upper() not in available_teams:
            return {
                "data": {
                    "error": "The team you query is unavailable. Check it again, please"
                }
            }
        requested_lol_stats = requested_lol_stats[
            requested_lol_stats["team"] == request_info["team"]
        ]

    requested_lol_stats = requested_lol_stats.to_json(orient="records")
    parsed = json.loads(requested_lol_stats)

    return {"data": parsed}, 200
