# 🔯 Relative Horoscope

<a href="https://relative-horoscope.herokuapp.com" target="_blank" >**Relative Horoscope**</a> not only provides your typical
daily forecast but analyzes how your luck fares compared to the remaining zodiac signs. On top of this, each sign
packs a dad joke which also updates daily so that you can leave the website with a hint of laughter (or perhaps an eye-roll 🙄).

## 🔨 Usage

On the <a href="https://relative-horoscope.herokuapp.com" target="_blank" >homepage</a>, find the zodiac sign that matches your birthday and click on the image to see your horoscope.
Refer to features section directly below for further explanation on each element on the page.

## 🎨 Features

1. Sentiment Analysis Score

   > A score between 0 to 100 that represents the analysis of the daily horoscope for the selected zodiac sign.
   > The higher the score, the more positive outlook. <a href="https://github.com/cjhutto/vaderSentiment" target="_blank">VADER Sentiment Analysis</a>,
   > known for accurately evaluating social media sentiments as well as plain short texts, is used to determine this score.
   > Think of this score as an absolute measurement of your today's luck.

2. Rank

   > Ranging from 1st to 12th, this rank is based on the Sentiment Analysis Score above.
   > Think of this rank as a relative measurement of your today's luck versus the remaining 11 zodiac signs.

3. Horoscope

   > This section includes the horoscope itself as well as the mood, lucky time, lucky number, color,
   > and the zodiac sign that has best compatibility for the day. The data is fetched from <a href="https://aztro.readthedocs.io/en/latest/" target="_blank">aztro REST API</a>.

4. Dad Joke of the Day

   > Fairly self-explanatory - a little brain teaser that may leave you with a laughter or an eye-roll.
   > The data is fetched from <a href="https://icanhazdadjoke.com">icanhazdadjoke API</a> and updates daily along
   > with the horoscope.

5. Social Media Share Buttons

   > Share buttons for Facebook and Twitter to let the world know about your fortune!

## 💻 Developers

To run this app locally, first install [Python 3](https://www.python.org/downloads/) then clone this repository:

```
git clone https://github.com/ysmike/relative-horoscope.git
```

Then install dependencies and run the app locally:

```
cd relative-horoscope && pip3 install -r requirements.txt && python3 app.py
```

Open a browser and enter the following in the address bar:

```
http://0.0.0.0:5000/
```

## 🔩 Built With

- [Flask](https://github.com/pallets/flask) - Web app framework
- [Jinja](https://www.palletsprojects.com/p/jinja/) - Template engine for Python
- [Bootstrap](https://getbootstrap.com/) - Toolkit for developing with HTML, CSS, and JS
- [aztro](https://aztro.readthedocs.io/en/latest/) - REST API for retrieving daily horoscopes
- [VADER](https://github.com/cjhutto/vaderSentiment) - Sentiment analysis tool
- [icanhazdadjoke](https://icanhazdadjoke.com) - API for retrieving dad jokes
