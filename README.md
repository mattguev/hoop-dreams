# Fantasy Basketball Game Predictor

## Motivation
Fantasy Basketball puts players in the shoes of a general manager (GM) building their team to compete over the course of an NBA season. But those shoes are tighter than most realize. In them, you are tasked with navigating the sort of questions that real GMs get paid millions to sort out alongside an office of professional coaches, trainers, and scouts: 

- "Which elite superstars can I build my team around?"
- "Do I trust Anthony Davis to stay healthy if I trade for him, maybe 3rd time's the charm?..."
- "How soon will it take this rookie to start impacting games?"
- "Is this player available because he's undervalued, or because people know something I don't?"
- "...aaand Anthony Davis is out for the season again."

Confronted with endless choices and forced to see the consequences play out in real-time, new managers quickly learn to put their money where their mouth is.

## The Rules (Head-to-Head, 9-Categories)
  - A league starts its season with managers each selecting ("drafting") 10-16 players. Draft order is based on a random draw.
  - Every week, managers are matched up with an opponent from their league.
  - Managers compete to win 9 categories: \
    _(Field Goal %, Free Throw %, 3-Pointers Made, Points, Rebounds, Assists, Steals, Blocks, Turnovers)_
  - You win each category (except for Turnovers) if your players produce more of that statistic relative to your opponent's players during the week's real-life games.
  - Winning each category is worth 1 point. A tie results in no points for either manager.
  - Managers can replace any player with a current active NBA player ("Free Agents"), provided that neither is currently mid-game. 

![](https://github.com/mattguev/hoop-dreams/blob/main/yfmatchup.JPG?raw=true)

## Game Theory and Adjustments

There are 9 ways to keep score in a game of fantasy basketball, compared to just 1 in real life. Out of these 9, you only need 5 to win.

One way to create a winning team is to use early draft picks on elite players who consistently dominate the league in correlated statistics. An example at the Guard position would be Steph Curry, whose [prolific ball handling and shooting](https://www.youtube.com/watch?v=7fPcse1phtk) enables him to produce huge Free Throw, Points, and 3-Point numbers on any given night. This individual greatness is made even greater by a [selfless willingness to pass](https://www.youtube.com/watch?v=rL_OflGAg1M) that makes him a great Assist vehicle.

An even better example, but at the Forward spot, is Nikola Jokic. Even at 6'11 and 284 lbs, he is able to [pass, shoot, and defend his position at elite levels](https://www.youtube.com/watch?v=hQQQDc98efQ). Over the course of a Fantasy season, he is consistently above average for Field Goals, Free Throws, Points, Rebounds, Assists, Steals, and Blocks--7 out of 9 categories!.

Yet, there are few of these stars by definition--[barely 20 players currently produce 1 standard deviation above the league average on at least 5 categories (i.e. category z-score > 1.0)](https://hashtagbasketball.com/fantasy-basketball-rankings). In a balanced 12-team league, this means you will have 2 at most. The remaining 11, you can draft based on how their skills fit alongside your superstar, your estimates of their growth trajectory, injury likelihood, etc. At the end of the draft, your roster will have 13 players. But, make no mistake, it is far from a finished product.

You enter your first matchup with a core group that collectively outperform the league in 5-7 categories, and a rotating cast of 2-3 players ("streamers") whose niche contributions can keep the team competitive during off nights. Managers are allowed a limited number of adds/drops ("streams") each week, so you can substitute these streamers for any available player without modifying your long-term strategy. All else equal, finding an advantage will come down to how you use these streamers. You can temporarily add them to pull away in a tightly contested category, substitute them for injured players, or in some rare cases even promote them into the core group. 

The caveat is that you can only decide on a specific tactic once you have a broad picture how your team will perform relative to your opponent for the week. That can be pretty difficult to do if this is what you're looking at:

![](https://github.com/mattguev/hoop-dreams/blob/main/yfmatchup2.JPG?raw=true)

Yikes. 

Yahoo's default tables are notoriously unhelpful for assessing comparative advantages. Furthermore, they don't let you compare "hypothetical team" performance (i.e. after certain roster adjustments) against other players. These features are locked behind a premium subscription.

## Audience and Features
Solution: Build a program that helps Yahoo Fantasy Basketball players with their roster decision-making by providing a basic matchup analysis feature--comparing two teams' expected statistical outputs and declaring the likely score.

## Datasets and Engineering 

The data for this project was scraped from the Yahoo Fantasy Basketball website using the [Yahoo Fantasy API](https://yahoo-fantasy-api.readthedocs.io/en/latest/introduction.html) ("YFA") and [Yahoo OAuth](https://pypi.org/project/yahoo-oauth/) Python packages.

The program is structured such that users must verify themselves via the Yahoo Email account they use to play Fantasy Basketball. Afterwards, the YFA package grants them access to fantasy information at various abstraction levels:
- Top level: Game class. A game, in the Yahoo! fantasy sense, is individual leagues you actively and historically participated in.
- Next level: League class. This is a particular instance of a game. It represents a particular season and game code that you played in. The league is found by its unique league ID.
- Next level: Team class. Within a league there are individual teams. The teams can be your own teams that you owned or one of your opponents.
- Lowest level: Players. Players either exist on a team or are free agents. There is no Player class to represent this level.

These levels are represented in Python using dictionaries of lists. For example, instances of the team class appear like this:

![](https://github.com/mattguev/hoop-dreams/blob/main/roster1.JPG?raw=true)

Data cleaning in this form consisted of the "stat_agg()" function which would index the necessary rosters and aggregate their season average statistics into a new dictionary:

![](https://github.com/mattguev/hoop-dreams/blob/main/cleanroster.JPG?raw=true)

## Results and Visualization

After cleaning the data, I designed a visualization function using Python's matplotlib where users can input the following parameters to produce a visualization similar to the one below: 
- League ID
- Aggregate Method (e.g. Season average, Last 30 Days, etc.)
- Team A
- Team B 

![](https://github.com/mattguev/hoop-dreams/blob/main/matchupviz1.JPG?raw=true)

The function is programmed with the Fantasy Basketball scoring rules detailed above, and users will be able to see the expected score between any two teams in the league based on their players' season averages. Having even a broad picture of the preliminary outcome against your opponent is crucial since it allows users to anticipate tightly contested categories, supplement their team with the appropriate streamers, and deny their opponent valuable resources. 

