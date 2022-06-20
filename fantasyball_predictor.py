'''Visualizing Fantasy Basketball Matchups

Question: Given two teams, which one is more likely to win based on the season average performance of its players?

Basic Features:
- Grouped horizontal bar charts (one for our team, another for our opponent's team)
- Predicted score

Datasets:
- Fantasy Basketball League Data (Yahoo API)

API Setup and Authentication:
- Create app on Yahoo Developer Network
- Follow quickstart directions from https://pypi.org/project/yahoo-oauth/ and save as 'oauth2.json' in working directory

In Terminal:
pip install yahoo_fantasy_api
pip install yahoo-oauth
pip install numpy
pip install matplotlib
'''

from yahoo_oauth import OAuth2 # documentation: https://pypi.org/project/yahoo-oauth/
import yahoo_fantasy_api as yfa # documentation: https://yahoo-fantasy-api.readthedocs.io/en/latest/index.html

import numpy as np
import matplotlib.pyplot as plt

# The YFA package grants users access to fantasy information at various abstraction levels:
# - Top level: Game class. A game, in the Yahoo! fantasy sense, is individual leagues you actively and historically participated in.
# - Next level: League class. This is a particular instance of a game. It represents a particular season and game code that you played in. The league is found by its unique league ID.
# - Next level: Team class. Within a league there are individual teams. The teams can be your own teams that you owned or one of your opponents.
# - Lowest level: Players. Players either exist on a team or are free agents. There is no Player class to represent this level.

# ## Loading Data Structures and Classes

# will be prompted to enter a security token after running this
sc = OAuth2(None, None, from_file="oauth2.json")
# 1st oauth parameter: consumer key
# 2nd oauth parameter: consumer secret

# get game object
gm = yfa.Game(sc, 'nba')
# 1st parameter: sc connection object
# 2nd parameter: sport code

# get league object
leagueid = '410.l.83755'  # AKPsi league

lg = gm.to_league(leagueid)  # pass desired league id

# get all team info
tms = lg.teams()

# get all team rosters
teamd = {}
for t in tms:
    teamd[f'{t}'] = []
    teamd[f'{t}'].append(tms[t]['name'])
    teamd[f'{t}'].append(lg.to_team(t).roster())

# ## Data Cleaning

# Helper function for aggregating a team's roster stats
def stat_agg(playerid: str) -> dict:
    agg_stats = {'TeamName': tms[playerid]['name'], 'FG%':0, 'FT%':0, '3PTPG':0, 'PPG':0, 'RPG':0,
                 'APG':0, 'SPG':0, 'BPG':0, 'TOPG':0}
    count = 0
    for p in teamd[playerid][1]:
        playstats = lg.player_stats([p['player_id']], 'average_season')[0]
        agg_stats['FG%'] = (count*agg_stats['FG%'] + 100*playstats['FG%'])/(count+1)
        agg_stats['FT%'] = (count*agg_stats['FT%'] + 100*playstats['FT%'])/(count+1)
        agg_stats['3PTPG'] += playstats['3PTM']
        agg_stats['PPG'] += playstats['PTS']
        agg_stats['RPG'] += playstats['REB']
        agg_stats['APG'] += playstats['AST']
        agg_stats['SPG'] += playstats['ST']
        agg_stats['BPG'] += playstats['BLK']
        agg_stats['TOPG'] += playstats['TO']
        count += 1

    return agg_stats

# Helper function for calculating the outcome of a matchup
def calc_outcome(p1stats, p2stats, participants) -> str:
    tallyA = 0
    tallyB = 0
    for i in range(len(p1stats)):
        if i < 8: 
            if p1stats[i] > p2stats[i]:
                tallyA += 1
            else:
                tallyB += 1
        elif i >= 8:
            if p1stats[i] < p2stats[i]:
                tallyA += 1
            else:
                tallyB += 1

    if tallyA > tallyB:
        return(f'{participants[0]} is expected to win against {participants[1]} with a score of {tallyA}-{tallyB}.')
    elif tallyA < tallyB:
        return(f'{participants[1]} is expected to win against {participants[0]} with a score of {tallyB}-{tallyA}.')
    else:
        return(f'{participants[0]} is expected to tie against {participants[1]} with an even score of {tallyA}-{tallyB}.')


# ## Visualization

def visualize_matchup(p1, p2): # player 1 and player 2
    p1_agg = stat_agg(p1)
    p2_agg = stat_agg(p2) 

    cats = list(p1_agg.keys())[1:] 
    p1_all = list(p1_agg.values())
    p2_all = list(p2_agg.values())

    matchup = [p1_all[0], p2_all[0]]
    p1_stats = p1_all[1:]
    p2_stats = p2_all[1:]
    
    # Horizontal Bar Chart
    x = np.arange(len(cats))
    width = 0.4

    fig, ax = plt.subplots() # specify which axes and figures to draw on
    bar1 = ax.barh(x + width/2, p1_stats[::-1], width, label = f'{matchup[0]}') # add horizontal bar to current axes
    bar2 = ax.barh(x - width/2, p2_stats[::-1], width, label = f'{matchup[1]}') 

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Category (Season Average)')
    ax.set_title('Matchup Analysis')
    ax.set_yticks(x, cats[::-1]) # reverse Category list for h-bars 
    ax.set_xticks([]) # remove x-ticks
    ax.legend()
    ax.bar_label(bar1, fmt = '%.3f', padding = 3) # set direct labels on the bars, format to 3 decimal places
    ax.bar_label(bar2, fmt = '%.3f', padding = 3)
    plt.text(65, 0.5, calc_outcome(p1_stats, p2_stats, matchup), fontsize = 12)

    fig.tight_layout()
    fig.set_size_inches(40, 5.5) # set figure (box) size in inches

    plt.show()

visualize_matchup('410.l.83755.t.10', '410.l.83755.t.7') # Joe Embiid vs. Martin's Team

