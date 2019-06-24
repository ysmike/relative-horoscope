import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer # VADER = Valence Aware Dictionary for sEntiment Reasoning

with open('adviceRanking.md','r') as f:
	content = f.readlines()
	content = [x.strip() for x in content]

sithlord = SentimentIntensityAnalyzer()

scores = []
for _ in content:
	# print(_, '\n', sithlord.polarity_scores(_))
	# print()
	sithlord.polarity_scores(_).append(scores)

	Don't give up your dreams & keep on sleeping. 
 {'neg': 0.0, 'neu': 0.722, 'pos': 0.278, 'compound': 0.4019}

Playing games vs. developing games is roughly equivalent to having sex vs. raising a child 
 {'neg': 0.0, 'neu': 0.878, 'pos': 0.122, 'compound': 0.2023}

If you are not happy where you are, move. Ya ain't no tree. 
 {'neg': 0.189, 'neu': 0.692, 'pos': 0.119, 'compound': -0.2755}

Life is a jar of cookies. Have the good ones first and buy a new jar. 
 {'neg': 0.0, 'neu': 0.818, 'pos': 0.182, 'compound': 0.4404}

Think like grandpa: "Grandpa, what do you think about premarital sex?" "Well, it's not premarital if you never get married" 
 {'neg': 0.0, 'neu': 0.884, 'pos': 0.116, 'compound': 0.3612}

Money can't buy you happiness, but at least you can be miserable in comfort. 
 {'neg': 0.305, 'neu': 0.536, 'pos': 0.158, 'compound': -0.461}

Never tell a woman she's overreating, or you'll see just how badly she can. 
 {'neg': 0.205, 'neu': 0.795, 'pos': 0.0, 'compound': -0.4767}

When in doubt, j**k off and think again. 
 {'neg': 0.263, 'neu': 0.737, 'pos': 0.0, 'compound': -0.3612}

Sing anything that is too stupid to be spoken. And you will have spoken it. 
 {'neg': 0.195, 'neu': 0.805, 'pos': 0.0, 'compound': -0.5267}

Give a man a fish and he will eat for a day. Deport a man and you will never have to feed him again -Trump 20:20 
 {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}

If you want to get rid of someone, loan them money 
 {'neg': 0.0, 'neu': 0.885, 'pos': 0.115, 'compound': 0.0772}

Fuck work hard and play hard. Work first and play later! 
 {'neg': 0.379, 'neu': 0.345, 'pos': 0.276, 'compound': -0.2003}

Your life might be better off incarcerating yourself. 
 {'neg': 0.0, 'neu': 0.707, 'pos': 0.293, 'compound': 0.4404}

Don't half-ass two things. Whole-ass one thing. -Ron Swanson 
 {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}

Don't make decisions without eating first. Follow this advice when choosing to eat. 
 {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}

Be medium. If both being high and being low are bad, what else can you do? 
 {'neg': 0.286, 'neu': 0.714, 'pos': 0.0, 'compound': -0.6808}

Don't sweat the petty things and don't pet the sweaty things. 
 {'neg': 0.0, 'neu': 0.863, 'pos': 0.137, 'compound': 0.1511}

You may not perish today. JK! 
 {'neg': 0.333, 'neu': 0.667, 'pos': 0.0, 'compound': -0.3612}

Don't worry about life. You're not gonna survive it anyways! 
 {'neg': 0.0, 'neu': 0.769, 'pos': 0.231, 'compound': 0.4015}

If you tend to fail at first, try skydiving. 
 {'neg': 0.304, 'neu': 0.696, 'pos': 0.0, 'compound': -0.5423}

I hope you don't play hide and seek because no one will bother to look for you. 
 {'neg': 0.301, 'neu': 0.499, 'pos': 0.2, 'compound': -0.3}

Statistics are like a bikini. What they reveal is interesting, but what they conceal is vital. 
 {'neg': 0.0, 'neu': 0.652, 'pos': 0.348, 'compound': 0.6597}

Keep a dictionary handy: the only place where success comes before work.
 {'neg': 0.0, 'neu': 0.73, 'pos': 0.27, 'compound': 0.5719}

Swim with a friend. Your chances of getting eaten by a shark will drop by 50%. 
 {'neg': 0.116, 'neu': 0.608, 'pos': 0.276, 'compound': 0.4404}

Don't let go of your girl's hand at the mall, or she will start shopping. 
 {'neg': 0.0, 'neu': 0.814, 'pos': 0.186, 'compound': 0.4939}
