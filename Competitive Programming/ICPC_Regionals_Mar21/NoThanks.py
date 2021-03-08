
'''
In the card game “No Thanks,” the deck of cards consists of 36 cards numbered 1–36, 
and players collect cards to their score pile as the game is played. A player’s final 
score is the sum of the numbers on their collected cards, with one exception: if a 
player has collected any cards with two or more consecutive numbers, only the smallest 
number of that group counts toward the score. Your job is to compute the score for a 
single player’s pile of cards, though here we allow play with a deck much larger than 
36 cards.

Input
The first line contains one integer, n, representing the number of cards collected. 
The second line contains n integers representing the numbers on the collected cards. 
You may assume that 1≤n≤90 000, all card values are in the range 1…90 000 inclusive, 
and no card value is repeated.

Output
The final score of the player
'''

n = int(input())
index = 0
cards = []
hold = 0
score = 0

cards = input().split()
for i in range(n):
    cards[i] = int(cards[i])
cards.sort()
# print(cards)
hold = cards[0]

for index in range(1,n):
    if cards[index]!=cards[index-1]+1:
        score+=hold
        hold = cards[index]
        if index == n-1:
            score+=hold
    elif index == n-1:
        score+=hold
if n==1:
    score = hold
    
print(score)