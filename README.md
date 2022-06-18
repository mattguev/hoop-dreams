# Fantasy Basketball Game Predictor

## Motivation
Fantasy Basketball puts players in the shoes of a general manager (GM), building their team to compete over the course of an NBA season. But not everyone realizes how tight those shoes can be. The game tasks its players with navigating the issues that real GMs get paid millions to figure out alongside an office of professional coaches, trainers, and scouts: 

- "Can I win if I build my team around this superstar's skillset?"
- "Do I trust Anthony Davis to stay healthy for the season if I draft him?"
- "How likely is this rookie to immediately make an impact?"
- "No seriously, Anthony Davis is available in the 4th round and I'm up next..."

New managers are constantly bombarded with decisions and forced to see the consequences play out in real-time. They learn, sooner or later, to put their money where their mouth is. And I love that. 

## The Rules
An overview of the format I play (Head-to-Head, 9-Categories):   
  - A league starts its season with managers each selecting ("drafting") 10-16 players. Draft order is based on a random draw.
  - Every week, managers are matched up with an opponent from their league.
  - Managers compete to win 9 categories: \
    _(Field Goal %, Free Throw %, 3-Pointers Made, Points, Rebounds, Assists, Steals, Blocks, Turnovers)_
  - You win each category (except for Turnovers) if your players produce more of that statistic relative to your opponent's players during the week's real-life games.
  - Winning each category is worth 1 point. A tie results in no points for either manager.
  - Managers can replace any player with a current active NBA player ("Free Agents"), provided that neither is currently mid-game. 

There are 9 ways to keep score in a game of fantasy basketball, compared to just 1 in real life. 


![](https://github.com/mattguev/hoop-dreams/blob/main/yfmatchup.JPG?raw=true)
     
From these 9, you only need 5 to win. Therefore, one strategy might be to focus on 5 or 6 stats. To do this effectively, however, you need to be able to compare how your players perform on average against your opponent's players. That can be difficult to do if this is what you're looking at:

![](https://github.com/mattguev/hoop-dreams/blob/main/yfmatchup2.JPG?raw=true)

Yikes. 

Yahoo's deafult tables are notoriously unhelpful for assessing comparative advantages. Furthermore, they don't let you compare "hypothetical team" performance (i.e. in the event of substituting players on your team for free agents) against other players. These more sophisticated visualizations and features are locked behind a premium subscription.

## Audience and Features
Solution: Build a program that unlocks a premium feature like basic matchup analysis--comparing two teams' expected statistical outputs and declaring the likely winner.

## Datasets and Engineering 

Building a Python program to model fantasy basketball games by using the Yahoo Sports API to scrape player statistics and calculate each team’s expected number 
