import requests
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer # VADER = Valence Aware Dictionary for sEntiment Reasoning

zodiacSigns = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']

descriptions = []
for zodiacSign in zodiacSigns:
    params = (('sign','{}'.format(zodiacSign)), ('day','today'))
    output = requests.post('https://aztro.sameerkumar.website/', params=params).json()
    descriptions.append(output['description'])

sithlord = SentimentIntensityAnalyzer()
for description in descriptions:
    scores = sithlord.polarity_scores(description)
    print(description, '\n', scores)
    print()

'''
You're going through some pretty weird interpersonal stuff right now, possibly with coworkers. It's one of those times when you need to stand your ground, even though you're not sure of yourself.
 {'neg': 0.102, 'neu': 0.809, 'pos': 0.089, 'compound': 0.1376}

You and your coworkers need to be wary of big risks today -- it's not that your luck is bad so much that you don't have all the info you need. Try to delay any gambles for a few more days at least.
 {'neg': 0.215, 'neu': 0.785, 'pos': 0.0, 'compound': -0.8548}

Someone very important decides to disagree with you -- maybe out of spite, or maybe legitimately. You should do your best to smooth over the argument for the time being, until you're on surer footing.
 {'neg': 0.185, 'neu': 0.631, 'pos': 0.185, 'compound': -0.0018}

Try not to worry too much about your surroundings or your people -- even if things seem really weird to you, you can still get a lot out of life and culture today. Keep your eyes and mind wide open!
 {'neg': 0.048, 'neu': 0.887, 'pos': 0.065, 'compound': 0.1791}

Try not to get too worked up over your own generosity -- it just happens, and there's not much you can do about it. You feel too good to worry about losing out in the long run, and that's not going to happen anyway.
 {'neg': 0.106, 'neu': 0.774, 'pos': 0.12, 'compound': 0.1779}

It's one of those days when you need to make sure that you're surrounded by your people -- though that is much easier than usual! Your good energy can turn almost anyone into a friend instantly.
 {'neg': 0.0, 'neu': 0.692, 'pos': 0.308, 'compound': 0.9067}

Your mind has taken a philosophical turn today, and you should find that you can come up with all sorts of great ideas as long as you keep your mind focused on the big picture in your life.
 {'neg': 0.0, 'neu': 0.839, 'pos': 0.161, 'compound': 0.7717}

Try to go along with the group today -- unless you need to avert disasters, of course! Most likely, they're bumbling along happily in more or less the right direction, and that's good enough for now.
 {'neg': 0.12, 'neu': 0.726, 'pos': 0.154, 'compound': 0.3595}

You're not really sure what's motivating you, but you know it doesn't matter! As long as you keep making progress today, you should be able to keep your people drafting along right behind you.
 {'neg': 0.069, 'neu': 0.771, 'pos': 0.16, 'compound': 0.6729}

No matter how tense things get today -- and depending on your people, they could get pretty ridiculous -- you still need to step up and take charge, or at least guide the situation to a successful conclusion.
 {'neg': 0.154, 'neu': 0.671, 'pos': 0.175, 'compound': 0.25}

You should find that your ability to communicate with your people is peaking today, and that they are giving you good news -- to say the least! At least one message coming your way thrills you.
 {'neg': 0.0, 'neu': 0.755, 'pos': 0.245, 'compound': 0.8553}

You're feeling more connected than ever to all the right people -- and are incredibly welcoming of new folks, too! It's a great time to think about your position in the big picture.
 {'neg': 0.0, 'neu': 0.761, 'pos': 0.239, 'compound': 0.8436}
 '''