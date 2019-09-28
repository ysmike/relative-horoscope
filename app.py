import datetime
import json
import os
from pprint import pprint
import requests

from flask import Flask, render_template, url_for
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import constants

app = Flask(__name__)

zodiac_cached = {}
last_cached_date = None


def cache_horoscope():
    global zodiac_cached
    global last_cached_date

    # check last cache date
    if last_cached_date != str(datetime.date.today()):
        ranks = []
        sithlord = SentimentIntensityAnalyzer()
        print("caching...")

        for sign in constants.zodiac_signs.keys():
            # fetch horoscopes
            params = (("sign", f"{sign}"), ("day", "today"))
            horoscope_data = requests.post(
                "https://aztro.sameerkumar.website/", params=params
            ).json()

            # sentiment analysis
            score = sithlord.polarity_scores(horoscope_data["description"])
            zodiac_cached[sign] = score

            # use 'compound' score, an aggregate of 'positive', 'negative', and 'neutral'
            ranks.append((score["compound"], sign))
            print(sign, "...done")

            horoscope = f"""{horoscope_data["description"]}<ul class="list-group list-group-flush">
                    <li class="list-group-item">Mood: {horoscope_data["mood"]}</li>
                    <li class="list-group-item">Lucky Time: {horoscope_data["lucky_time"]}</li>
                    <li class="list-group-item">Lucky Number: {horoscope_data["lucky_number"]}</li>
                    <li class="list-group-item">Color: {horoscope_data["color"]}</li>
                    <li class="list-group-item">Compatibility: {horoscope_data["compatibility"]}</li>
                    </ul>"""

            zodiac_cached[sign].update(
                {"horoscope": horoscope, "date": constants.zodiac_signs[sign]}
            )

        # populate rank
        rank = 0
        ranks.sort(key=lambda x: x[0], reverse=True)

        # fetch dad jokes
        jokes_data = {}
        while len(jokes_data) < 12:
            joke = requests.get(
                "https://icanhazdadjoke.com/", headers={"Accept": "application/json"}
            ).json()
            if joke["id"] not in jokes_data:
                jokes_data[joke["id"]] = joke["joke"]
        jokes = list(jokes_data.values())

        # assign ranks, colors, dad jokes
        for _, sign in ranks:
            zodiac_cached[sign].update(
                {
                    "rank": rank + 1,
                    "color": constants.ordinal_rank_colors[rank],
                    "joke": jokes[rank],
                }
            )
            rank += 1

        # save the cache date
        last_cached_date = str(datetime.date.today())
        # pprint(zodiac_cached)


@app.route("/<sign>")
def horoscope(sign):
    # check url
    if sign not in constants.zodiac_signs:
        return json.dumps({"Message": "The provided sign does not exist!"})

    # get logo
    logo = url_for("static", filename="img/" + (sign.lower()) + "-759.jpg")

    # call cacher
    cache_horoscope()

    # change numbers from cardinals to ordinals
    ordinal = (
        lambda n: f"""{n}{ {1:"st",2:"nd",3:"rd"}.get(n if n < 20 else n % 10, "th") }"""
    )

    normalize = lambda n: int((((n - (-1)) * (100 - 0)) / (1 - (-1))) + 0)

    colorize = (
        lambda n: constants.cardinal_rank_colors[-(n // 10 + 1)]
        if n in range(101)
        else None
    )

    # fetch horoscope from API
    return render_template(
        "horoscope.html",
        zodiac_sign=sign,
        zodiac_logo=logo,
        details=zodiac_cached[sign],
        ordinal=ordinal,
        normalize=normalize,
        colorize=colorize,
    )


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
