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

blunt_predictions = [
    "Life is a jar of cookies. Have the good ones first and buy a new jar!",
    "Don't give up your dreams & keep on sleeping ;)",
    "Don't worry about life. Nobody survives it anyways!",
    "Sing anything that is too stupid to be spoken. And you will have spoken it.",
    "Don't half-ass two things. Whole-ass one thing. -Ron Swanson",
    "Money can't buy you happiness, but at least you can be miserable in comfort.",
    "When in doubt, j**k off and think again.",
    "Phuq work hard and play hard. Work first and play later!",
    "Don't make decisions without eating first. Follow this advice when choosing to eat.",
    "Be medium. If both being high and being low are bad, what else can you do?",
    "I hope you don't play hide and seek because no one will bother to look for you :(",
    "If you tend to fail at first, perhaps try skydiving :)",
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
            # fetch horoscope
            params = (("sign", f"{sign}"), ("day", "today"))
            data = requests.post(
                "https://aztro.sameerkumar.website/", params=params
            ).json()

            horoscope = f"""{data["description"]}<ul>
                    <li>Mood: {data["mood"]}</li>
                    <li>Lucky Time: {data["lucky_time"]}</li>
                    <li>Lucky Number: {data["lucky_number"]}</li>
                    <li>Color: {data["color"]}</li>
                    <li>Compatibility: {data["compatibility"]}</li>
                    </ul>"""

            zodiac_cached[sign] = {"horoscope": horoscope, "date": zodiac_signs[sign]}

            # sentiment analysis
            score = sithlord.polarity_scores(data["description"])
            zodiac_cached[sign].update(score)

            # use 'compound' score, an aggregate of 'positive', 'negative', and 'neutral'
            ranks.append((score["compound"], sign))
            print(sign, "...done")

        # populate rank
        rank = 0
        ranks.sort(key=lambda x: x[0])
        for _, sign in ranks:
            zodiac_cached[sign].update(
                {
                    "rank": rank + 1,
                    "color": rank_colors[rank],
                    "blunt": blunt_predictions[rank],
                }
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

    # fetch horoscope from API
    return render_template(
        "horoscope.html",
        zodiac_sign=sign,
        zodiac_logo=logo,
        details=zodiac_cached[sign],
    )


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
