import pandas as pd
import requests as rq
from bs4 import BeautifulSoup

get_url = rq.get("https://www.msn.com/en-us/sports/soccer/la-liga/player-stats")

get_text = get_url.text

soup = BeautifulSoup(get_text, "html.parser")

rank = [i.text for i in soup.findAll('td', {
    "class": "hide1 rankvalue"
})]

player_name = [i.text
               for i in soup.findAll('td', {
        "class": "playername"
    })
               ]

team_name = [i.text
             for i in soup.findAll('td', {
        "class": "teamname"
    })
             ]

team_la = [i.text
           for i in soup.findAll('td', {
        "class": "teamtla"
    })
           ]

games_played = [int(i.findAll('td')[4].text) for i in soup.findAll('tr', {
    "class": "rowlink"
})]

goals_scored = [int(i.findAll('td')[7].text) for i in soup.findAll('tr', {
    "class": "rowlink"
})]

assists = [int(i.findAll('td')[8].text) for i in soup.findAll('tr', {
    "class": "rowlink"
})]

laliga_stats = pd.DataFrame({

    "Rank": rank,

    "Player Name": player_name,

    "Team Name": team_name,

    "Team": team_la,

    "Games Played": games_played,

    "Goals": goals_scored,

    "Assists": assists

})

laliga_stats[0:10]

goals_percentile_top10 = laliga_stats['Goals'][0:10].sum() * 100 / laliga_stats['Goals'].sum()
goals_percentile_top10

laliga_stats['Goals'].sum()

laliga_stats[laliga_stats['Goals'].isin([1])]

team_stats = laliga_stats.groupby(['Team'])['Goals', 'Assists'].sum()
team_stats.sort_values('Goals', ascending=False)
