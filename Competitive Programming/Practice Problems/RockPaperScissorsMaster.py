# Rock Paper Scissors Master
'''
Rock-paper-scissors is a popular two-player game. In the game, each of the 
players uses their hand to show one of three symbols: rock, paper or scissors. 
If both players show the same symbol, the game is a tie. Otherwise, scissors 
beat paper, paper beats rock and rock beats scissors.

Sven has been studying the psychological intricacies of the game for years and 
has become a real master at the game, his friends not standing a chance 
against him in one-on-one games.

With the world championships around the corner, Sven is practicing his skills 
playing simultaneous games with N of his friends. One such game consists of R 
rounds. In each round, Sven and each of his friends show one of the three 
symbols.

When calculating the score, in each round, Sven’s symbol is independently 
compared to each of his friends’ symbols. Sven scores two points for every 
win and one point for every tie. Sven does not get points for losing.

Write a program that calculates Sven’s total score, and also his largest 
possible score had he known in advance all the symbols his friends would 
show.
'''
# get all necessary info from user
rounds = int(input())
my_moves = input()
num_enemies = int(input())
enemy_moves = []

# initialize all necessary variables
index = 0
rcount = 0
pcount = 0
scount = 0
score = 0
best = 0
bestOfRound = []

for index in range(num_enemies):
    enemy_moves.append(input())

for index in range(rounds): # this loop checks for my wins/ties/losses
    for enemy in enemy_moves:
        move = enemy[index]
        my_move = my_moves[index]
        if move=='R':
            rcount+=1
            if my_move=='R':
                score+=1
            elif my_move=='P':
                score+=2
            elif my_move=='S':
                continue
        elif move=='P':
            pcount+=1
            if my_move=='R':
                continue
            elif my_move=='P':
                score+=1
            elif my_move=='S':
                score+=2
        elif move =='S':
            scount+=1
            if my_move=='R':
                score+=2
            elif my_move=='P':
                continue
            elif my_move=='S':
                score+=1
    bestOfRound.append(2*rcount+pcount) # score if I chose paper
    bestOfRound.append(2*pcount+scount) # score if I chose scissors
    bestOfRound.append(2*scount+rcount) # score if I chose rock
    bestOfRound.sort()
    best+=bestOfRound[-1]
    rcount = 0
    pcount = 0
    scount = 0
    bestOfRound.clear()

print("My score: {}".format(score))
print("Best possible score: {}".format(best))
print(f"Best possible score: {best}")