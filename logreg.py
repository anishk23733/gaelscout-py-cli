from raschietto import Raschietto, Matcher
import pandas as pd
from collect import collect

df = pd.read_pickle("team_dataframes/teamList.pkl")

teamList = df["Team Number: "].tolist()

# List of lists, [[Ranks, MaxScores, OPRs], [Ranks, MaxScores, OPRs]... ]
# teamStats = []
# for team in teamList:
#     teamStats.append(collect(team))

for teamName in teamList:
    url = "https://vexdb.io/teams/view/{}?t=results".format(teamName)
    page = Raschietto.from_url(url)
    results = Matcher('.result-red')
    results = results(page, multiple=True)

    blueScores = []
    blueAlliance1 = []
    blueAlliance2 = []

    redScores = []
    redAlliance1 = []
    redAlliance2 = []
    print(url)
    print(results)
    # for i in range(len(results)):
    #     if (i+1) % 6 == 0:
    #         blueScores = results[i]
    #         redScores = results[i-1]
    #         blueAlliance1 = results[i-3]
    #         blueAlliance2 = results[i-2]
    #         redAlliance1 = results[i-5]
    #         redAlliance2 = results[i-4]
    #
    #         winloss = []
    #
    #         if teamName == blueAlliance1 or teamName == blueAlliance2:
    #             if blueScores > redScores:
    #                 winloss.append(1)
    #             else:
    #                 winloss.append(0)
    #         elif teamName == redAlliance1 or teamName == redAlliance2:
    #             if redScores > blueScores:
    #                 winloss.append(1)
    #             else:
    #                 winloss.append(0)
    #
    #         print(blueAlliance1, blueAlliance2, redAlliance1, redAlliance2, blueScores, redScores, winloss)
