import random, sys
print('ROCK,PAPER,SCISSORS')
#this variables keeo track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0
while True:#the main game loop.
    print('%s Wins,%s Losses,%s Ties'%(wins,losses,ties))
    while True: #the player input loop
        print('enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() #quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # break out of input loop
    print('type one of r,p,s or q.')
    #display what the player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')
    #display what computer chose
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == '3':
        computerMove = 's'
        print('SCISSORS')
    #display and record the win/loss/ties:
    if playerMove == computerMove:
        print('its a tie')
        ties = ties +1
    elif playerMove == 'r' and computerMove == 's':
        print('you win')
        wins = wins +1
    elif playerMove == 'p' and computerMove == 'r':
        print('you win')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('you win')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'P':
        print('you lose')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('you lose')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('you lose')
        losses = losses + 1