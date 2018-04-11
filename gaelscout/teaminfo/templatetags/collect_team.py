from django import template
from raschietto import Raschietto, Matcher

register = template.Library()
@register.filter(name='collect')
def collect(data, team_num):
    scores = Raschietto.from_url("https://vexdb.io/teams/view/{}?t=rankings".format(team_num))

    rankPointer = Matcher('.rank')
    ranksList = rankPointer(scores, multiple=True)
    try:
        ranksList.remove(ranksList[0])
    except: pass
    try:
        ranksList = list(map(int, ranksList[0:7]))
    except:
        ranksList = list(map(int, ranksList))

    maxScorePointer = Matcher('.max_score')
    maxScoreList = maxScorePointer(scores, multiple=True)
    try:
        maxScoreList.remove(maxScoreList[0])
        try: maxScoreList = list(map(int, maxScoreList[0:7]))
        except: maxScoreList = list(map(int, maxScoreList))
    except: pass

    OPRPointer = Matcher('.opr')
    OPRList = OPRPointer(scores, multiple=True)
    try:
        OPRList.remove(OPRList[0])
        try: OPRList = list(map(float, OPRList[0:7]))
        except: OPRList = list(map(float, OPRList))
    except: pass

    return [ranksList, maxScoreList, OPRList]
