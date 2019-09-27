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

ordinal_rank_colors = [
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
    "#fb5a49",
    "#AD0000",
]

cardinal_rank_colors = [
    "#3A6C4D",
    "#458257",
    "#5A9951",
    "#A4C064",
    "#EEE277",
    "#EBBC4F",
    "#F1AC47",
    "#F77023",
    "#fb5a49",
    "#AD0000",
]

# Find matching color based on the sentiment analysis score
def colorize(n):
    if 0 <= n <= 100:
        return cardinal_rank_colors[-(n // 10 + 1)]
