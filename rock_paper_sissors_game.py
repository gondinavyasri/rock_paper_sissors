a=['player1','player2']
print('rock paper or scissor?')
player1_score=0
player2_score=0
for i in range(1,6):
    player1=input('player 1:')
    player2=input('player 2:')
    if(player1=='rock' and player2=='paper'):
        print('player2 wins!')
        player2_score=player2_score+1
    elif(player1=='rock' and player2=='scissors'):
        print('player1 wins!')
        player1_score=player1_score+1
    elif(player1=='paper' and player2=='rock'):
        print('player1 wins!')
        player1_score=player1_score+1
    elif(player1=='paper' and player2=='scissors'):
        print('player2 wins!')
        player2_score=player2_score+1
    elif(player1=='scissors' and player2=='rock'):
        print('player2 wins!')
        player2_score=player2_score+1
    elif(player1=='scissors' and player2=='paper'):
        print('player1 wins!')
        player1_score=player1_score+1
    else:
        print('tie!')
    print('player1 score is',player1_score)
    print('player2 score is',player2_score)
if(player1_score>player2_score):
    print('player1 wins!')
else:
    print('player2 wins!')
