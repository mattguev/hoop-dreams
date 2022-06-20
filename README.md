# Fantasy Basketball Game Predictor

## Motivation
Fantasy Basketball puts players in the shoes of a general manager (GM) building their team to compete over the course of an NBA season. But not everyone realizes how tight those shoes can be. Players are tasked with navigating the sort of questions that real GMs get paid millions to figure out alongside an office of professional coaches, trainers, and scouts: 

- "Which superstar can I build my team around?"
- "Do I trust Anthony Davis to stay healthy if I trade for him?..."
- "How soon will it take this rookie to figure things out and start impacting games?"
- "Is this player available right now because he's undervalued, or because people know something I don't?"
- "...aaand Anthony Davis is out for the season again, which Free Agents can I drop him for?"

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

You enter your first matchup with a core group that collectively outperform the league in 5-7 categories, and a rotating cast of 2-3 players whose niche contributions can keep the team competitive on off nights ("streamers"). Managers are allowed a limited number of player adds/drops ("streams") each week, so you can substitute these streamers for any free agent without worrying about your long-term strategy. All else equal, finding an advantage will come down to how you use these streamers. You can add them temporarily to pull away in a tightly contested category, supplement injured players from the core group, or in some rare cases even promote them into the core group. 

You can only decide on who you want to use, and how, once you compare how your team performs on average relative to your opponent's players for the week. That can be difficult to do if this is what you're looking at:

![](https://github.com/mattguev/hoop-dreams/blob/main/yfmatchup2.JPG?raw=true)

Yikes. 

Yahoo's deafult tables are notoriously unhelpful for assessing comparative advantages. Furthermore, they don't let you compare "hypothetical team" performance (i.e. after certain roster adjustments) against other players. These more sophisticated visualizations and features are locked behind a premium subscription.

## Audience and Features
Solution: Build a program that provides a premium function like basic matchup analysis--comparing two teams' expected statistical outputs and declaring the likely winner. This program can also model matchups, accounting for certain hypothetical roster adjustments.


## Datasets and Engineering 

Building a Python program to model fantasy basketball games by using the Yahoo Sports API to scrape season averages (or last* interval stats to avoid low-GP outliers) and calculate each team’s expected number of points.
