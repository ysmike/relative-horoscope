import datetime
import json
from pprint import pprint
import requests

from flask import Flask, render_template, url_for
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

zodiac_signs = {
    "Aries": "Mar 21 - Apr 19",
    "Taurus": "Apr 20 - May 20",
    "Gemini": "May 21 - June 20",
    "Cancer": "June 21 - July 22",
    "Leo": "July 23 - Aug 22",
    "Virgo": "Aug 23 - Sept 22",
    "Libra": "Sept 23 - Oct 22",
    "Scorpio": "Oct 23 - Nov 21",
    "Sagittarius": "Nov 22 - Dec 21",
    "Capricorn": "Dec 22 - Jan 19",
    "Aquarius": "Jan 20 - Feb 18",
    "Pisces": "Feb 19 - Mar 20",
}

rank_colors = [
    "#3A6C4D",
    "#458257",
    "#5A9951",
    "#7EA95A",
    "#A4C064",
    "#E3EE77",
    "#EEE277",
    "#EBBC4F",
    "#F1AC47",
    "#F77023",
    "#F86135",
    "#AD0000",
]

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

        for sign in zodiac_signs.keys():
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
                    <li class="list-group-item">Sentiment Analysis Score: {zodiac_cached[sign]["compound"]}</li>
                    <li class="list-group-item">Mood: {horoscope_data["mood"]}</li>
                    <li class="list-group-item">Lucky Time: {horoscope_data["lucky_time"]}</li>
                    <li class="list-group-item">Lucky Number: {horoscope_data["lucky_number"]}</li>
                    <li class="list-group-item">Color: {horoscope_data["color"]}</li>
                    <li class="list-group-item">Compatibility: {horoscope_data["compatibility"]}</li>
                    </ul>"""

            zodiac_cached[sign].update(
                {"horoscope": horoscope, "date": zodiac_signs[sign]}
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
                {"rank": rank + 1, "color": rank_colors[rank], "joke": jokes[rank]}
            )
            rank += 1

        # save the cache date
        last_cached_date = str(datetime.date.today())
        pprint(zodiac_cached)


@app.route("/<sign>")
def horoscope(sign):
    # check url
    if sign not in zodiac_signs:
        return json.dumps({"Message": "The provided sign does not exist!"})

    # get logo
    logo = url_for("static", filename="img/" + (sign.lower()) + "-759.jpg")

    # call cacher
    cache_horoscope()

    # change numbers from cardinals to ordinals
    ordinal = (
        lambda n: f"""{n}{ {1:"st",2:"nd",3:"rd"}.get(n if n < 20 else n % 10, "th") }"""
    )

    # fetch horoscope from API
    return render_template(
        "horoscope.html",
        zodiac_sign=sign,
        zodiac_logo=logo,
        details=zodiac_cached[sign],
        ordinal=ordinal,
    )


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
