# Fantasy Basketball Game Predictor

## Motivation
Fantasy Basketball puts players in the shoes of a general manager (GM), building their team to compete over the course of an NBA season. But not everyone realizes how tight those shoes can be. The game tasks its players with navigating the sort of issues that real GMs get paid millions to figure out alongside an office of professional coaches, trainers, and scouts: 

- "Can I win if I build my team around this superstar's skillset?"
- "Do I trust Anthony Davis to stay healthy for the season if I draft him?"
- "How likely is this rookie to immediately make an impact?"
- "No seriously, Anthony Davis is still available in the 4th round and I'm up next..."

Someone playing in their first league is constantly bombarded with decisions and forced to see the consequences play out in real-time. They learn, sooner or later, to put their money where their mouth is. And I love that.

## The Rules
An overview of the format I play (Head-to-Head, 9-Categories): 

  ![](https://github.com/mattguev/hoop-dreams/blob/main/yfmatchup.JPG?raw=true)
  
  - A league starts its season with managers each selecting ("drafting") 10-16 players. Draft order is based on a random draw.
  - Every week, managers are matched up with an opponent from their league.
  - Managers compete to win 9 categories \
    _(Field Goal %, Free Throw %, 3-Pointers Made, Points, Rebounds, Assists, Steals, Blocks, Turnovers)_
  - You win each category (except for Turnovers) if your players produce more of that statistic relative to your opponent's players during the week's real-life games.
  - Winning each category is worth 1 point. A tie results in no points for either manager.
  - Managers can replace any player with a current active NBA player ("Free Agents"), provided that neither are currently mid-game. 

## The Data


   
  ![](https://github.com/mattguev/hoop-dreams/blob/main/yfmatchup2.JPG?raw=true)
  
  Narrowing the game to 9-scoring categories and removing the intangibles,
  
  For example, players with limited resources can still develop a competitive advantage by focusing on 5 key categories at the cost of the other 4. This  is a large competitive advantage to be had in  Visualizations and advanced statistics are locked behind a premium subscription

  
## Audience and Features
Solution: Build a program that unlocks a premium feature like basic matchup analysis--comparing two teams' expected statistical outputs and declaring the likely winner.



Building a Python program to model fantasy basketball games by using the Yahoo Sports API to scrape player statistics and calculate each team’s expected number 
