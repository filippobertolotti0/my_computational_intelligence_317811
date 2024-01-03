# LAB 10: Play Tic-Tac-Toe with Reinforcement Learning

Implementation of an algorithm based on reinforcement learning capable to play Tic-Tac-Toe against a reinforced random player starting from zero knowledge about winning strategy.

## Introduction

Firstly i have created a class called History. This class contains:

 - The state of X player
 - The state of O player
 - A table where each available move is associated to reward

The reinforcement learning player (RL_player) based its strategy on an array of "History" elements. Each element describes a different state of the game.

The two players play 1_000_000 games of training meanwhile the RL_player improve its strategy, than they will play 100 games of "real game" after that we obtain the results. 

## Strategy Adopted

Prevoiuosly i called the random_player as "reinforced random_player" because in case it will have a winning move it will choose that specific move in order to win the game, so in these states it will not play randomly.

The RL_player initially play completely randomly but after every move, if not already present, he add the current state into the history array. In case the current state is already into the history the RL_player will choose one of the available move with the highest reward from the respective table.

After every winning move, both side, the algorithm will performs an update on the rewards table of the last state of RL_player. So there are two possibilities:

- random_player win: means that RL_player's last move was bad and maybe he could block his enemy so that move get a -1 on its reward table.
- RL_player win: means that RL_player's last move was a winning move so that move get a +2 on its reward table.

## Conclusions

After the training the RL_player has an average win ratio of 80% while the random_player has an average win ratio less than 10%.

## Peer Reviews

https://github.com/gregorio-nic/computational-intelligence/issues/5
https://github.com/ludofiorio/labs_comp_inte/issues/9
