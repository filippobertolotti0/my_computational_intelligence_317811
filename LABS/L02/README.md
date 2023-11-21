# Lab 2: Nim
Implementation of an evolutionary algorithm capable to play the Nim game.
## Individuals, Parameters and Population
The class "individual" will play the part of genome in my evolutionary algorithm.

An individual consists in a counter "wins" taking notes of number of matches won by the individual and a set of parameters:
- odd: number of rows with odd number of elements.
- firstlast: probability to pick elements from the first.
- k: probability to pick all the row's elements.

The starting population is composed by 100 individuals having randomly parameters (each from 0 to 1) and counter initialized to 0.

## Strategy adopted
The evolutionary strategy is based on a tournament between the 100 individuals. Every individual play against each other two times (198 matches each). The winner's counter is increased everytime a match end up.

I sort the population in terms of won matches and discard the worst 50 individuals. The best 50 individuals are passed to the "mutation" function which randomly change the parameters of every individual and reset the the counters.

I generate 50 new players each picking up randomly two parents from the bests individuals and create a new set of parameters choosing randomly from the parents' ones.

At the end i let the best one individual play against the Optimal and the Random players 1000 times each and compare the results with a threshold, if the results are not good enough the algorithm restart.

## Conclusions
The evolutionary strategy in few minutes returns a player with an average win percentage of:
- 66% against the pure random player.
- 40% against the optimal player.

As i seen the results are not perfect but with the introduction of some more parameters i think that the strategy could reach at least an average of 75% and 48% respectively against random and optimal players.