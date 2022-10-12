# Fantasy Basketball Game Predictor

## Motivation
Fantasy Basketball puts players in the shoes of a general manager (GM) building their team to compete over the course of an NBA season. In them, you are tasked with answering hard questions that real GMs get paid millions to navigate alongside an office of professional coaches, trainers, and scouts: 

- "Which elite superstars can I build my team around?"
- "What's a reasonable projection for this rookie's first year stats?"
- "What tradeoffs am I willing to make between consistency and upside?"
- "Is this player available to me because he's undervalued, or because people know something I don't?"

Confronted with endless choices and forced to see the consequences play out in real-time, new managers quickly learn to put their money where their mouth is.

## The Rules (Head-to-Head, 9-Categories)
  - A league starts its season with a draft where managers take turns selecting players to form their roster. Initial draft order is based on a random draw.
  - Every week, managers are matched up with an opponent from their league.
  - Managers compete across up to 9 categories: \
    _(Field Goal %, Free Throw %, 3-Pointers Made, Points, Rebounds, Assists, Steals, Blocks, Turnovers)_
  - You win a category if your players produce more of that statistic relative to your opponent's players during the week's real-life games. The opposite is true for Turnovers which are won by the manager with less of them. 
  - Winning each category is worth 1 point. A tie results in no points for either manager.
  - Managers can replace any player with a current active NBA player ("Free Agents"), provided that neither is currently mid-game. 

![](https://github.com/mattguev/hoop-dreams/blob/main/yfmatchup.JPG?raw=true)

## Game Theory and Adjustments

There are 9 ways to keep score in a game of fantasy basketball, compared to just 1 in real life. Out of these 9, you only need 5 to win.

One way to create a winning team is to use early draft picks on elite players who consistently dominate the league in correlated statistics. One example would be Stephen Curry, whose [ball handling and shooting](https://www.youtube.com/watch?v=7fPcse1phtk) gives you great Free Throw, Points, and 3-Point numbers on any given night. Combining the resultant ["gravitational effect"](https://www.youtube.com/watch?v=lh8s93wXkCc) with his [willingness to pass](https://www.youtube.com/watch?v=rL_OflGAg1M) to open teammates, he is also a decent Assists vehicle.

An more outrageous example is Nikola Jokic. Even at 6'11 and 284 lbs, he is able to [pass, shoot, and defend his position at elite levels](https://www.youtube.com/watch?v=hQQQDc98efQ). Over the course of a Fantasy season, he is well above the league average for Field Goals, Free Throws, Points, Rebounds, Assists, Steals, and Blocks--7 out of 9 categories!.

Yet, there are few of these stars by definition--[barely 20 players currently produce 1 standard deviation above the league average on at least 5 categories (i.e. category z-score > 1.0)](https://hashtagbasketball.com/fantasy-basketball-rankings). In a balanced 12-team league, this means you will have 2 at most. The remaining 11, you can draft based on how their skills fit alongside your superstar, estimates of their growth trajectory, injury likelihood, etc. At the end of the draft, your roster will have around 13 players. But, make no mistake, it is far from a finished product.

You enter your first matchup with a core group that collectively outperforms the league in 5-7 categories, and a rotating cast of 2-3 players ("streamers") whose niche contributions can keep the team competitive during off nights. Managers are allowed a limited number of adds/drops ("streams") each week, so you can substitute these streamers for any available player without modifying your long-term strategy. All else equal, finding an advantage will come down to how you use these streamers. You can temporarily add them to pull away in a tightly contested category, substitute them for injured players, or in some rare cases even promote them into the core group. 

The problem is that you can only decide on a specific tactic once you have a broad picture how your team will perform relative to your opponent for the week. That can be a difficult task if this is what you're looking at:

![](https://github.com/mattguev/hoop-dreams/blob/main/yfmatchup2.JPG?raw=true)

Yikes. 

Yahoo's default tables are notoriously unhelpful for assessing comparative advantages. Furthermore, they don't let you compare projected statistics (e.g. after certain roster adjustments) against other players. These features are locked behind a premium subscription.

## Audience and Features
Solution: Build a program that helps Yahoo Fantasy Basketball players with their roster decision-making by providing a basic matchup analysis feature--comparing two teams' expected statistical outputs and declaring the likely score.

The program will be designed with the Fantasy Basketball scoring rules detailed above, and users will be able to see the expected score between any two teams in the league based on their players' projected or actual season averages. Having even a broad picture of the preliminary outcome against your opponent is crucial since it allows users to anticipate tightly contested categories, supplement their team with the appropriate streamers, and deny their opponent valuable resources. 

## Datasets and Engineering 

The data for this project was scraped from the Yahoo Fantasy Basketball website using the [Yahoo Fantasy API](https://yahoo-fantasy-api.readthedocs.io/en/latest/introduction.html) ("YFA") and [Yahoo OAuth](https://pypi.org/project/yahoo-oauth/) Python packages.

The program is structured such that users must verify themselves via the Yahoo Email account they use to play Fantasy Basketball. Afterwards, the YFA package grants them access to fantasy information at various abstraction levels:
- Top level: Game class. A game, in the Yahoo! fantasy sense, is individual leagues you actively and historically participated in.
- Next level: League class. This is a particular instance of a game. It represents a particular season and game code that you played in. The league is found by its unique league ID.
- Next level: Team class. Within a league there are individual teams. The teams can be your own teams that you owned or one of your opponents.
- Lowest level: Players. Players either exist on a team or are free agents. There is no Player class to represent this level.

These levels are represented in Python using dictionaries of lists. For example, instances of the team class appear like this:

![](https://github.com/mattguev/hoop-dreams/blob/main/roster1.JPG?raw=true)

Data cleaning in this case consisted of a custom-designed statistics aggregator "stat_agg()" function which would index the necessary rosters and aggregate their season average statistics into a new dictionary like the one below:

![](https://github.com/mattguev/hoop-dreams/blob/main/cleanroster.JPG?raw=true)

## Results and Visualization

After cleaning the data, I designed a visualization function using Python's matplotlib where users can input the following parameters to produce a visualization similar to the one below: 
- League ID
- Aggregate Method (e.g. Season average, Last 30 Days, etc.)
- Team A
- Team B 

![](https://github.com/mattguev/hoop-dreams/blob/main/matchupviz1.JPG?raw=true)

Here, we see Joe Embiid (my team) is expected to win 5-4 against my opponent for the week. Yet, 3 tightly contested categories (Field Goal %, Steals, and Turnovers) can easily reverse that outcome. As a result, I might drop a few of my streamers to pick up a Forward or Center. Their close proximity to the rim and minimal passing responsibility usually results in a higher Field Goal %, lower Turnovers, and even the occasional Steal. Someone like Larry Nance, Jr. fits that description perfectly. We could add him and run the matchup analysis again to see how the outlook changes. 

## Conclusion
It's ultimately important to remember that data and prediction are merely tools for decision making. This program can't tell managers exactly who to add and when for a sure victory, but it can significantly narrow down their choices so they get closer to making the right ones.
