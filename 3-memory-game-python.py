#Course: ITI 1120

#########################################################################
#PLEASE IGNORE COMMENTS, I PUT THEM ONLY TO HELP ME WHILE IM PROGRAMMING
#########################################################################

import random #used to shuffle the board

def create_board(size):
    '''int->list (of str)
       Precondition: size is even positive integer between 2 and 52    
    '''
    board = [None]*size 

    letter='A'
    for i in range(len(board)//2):
          board[i]=letter
          board[i+len(board)//2 ]=board[i]
          letter=chr(ord(letter)+1)
    random.shuffle(board)
    return board

def print_board(a):
    #i noticed that this function was given to us, but isn't necessary
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')


def wait_for_player():
    '''(None)->None
    Pauses the program until the user presses enter
    '''
    #if you do not pause the game in certain situation,
    #player will not be able to see cards revealed
    #because two new locations will have already gone from the screen
    try:
        input("Press enter to continue ")
    except SyntaxError:
        pass

def play_game(board):
    '''(list of str)->None'''
    # The following line of code creates a list indicating what locations are paired, i.e., discovered
    # At the begining none are, so default initializaiton to False is ok
    # You may find this useful
    discovered =[False]*len(board)

   # YOUR CODE GOES HERE
   # this is the funciton that plays the game
    NumbGuesses =0
    while discovered != [True]*len(board):    
        print_boardv2(board, discovered)
        #guess1 =0
        #guess2 =0
        print("Enter two distinct locations on the board that you want revealed.\ni.e two integers in the range [1, "+str(size)+"]")   
        guess1 = int(input("First:  "))
        guess2 = int(input("Second: "))
        NumbGuesses += 1
        
        while (guess1>size or guess1<1 or guess1==guess2 or guess2>size or guess2<1):
            #print("'Invalid input'") #NOT necessary but can be helpful to the user in my program
            print("Enter two distinct locations on the board that you want revealed.\ni.e two integers in the range [1, "+str(size)+"]")   
            guess1 = int(input("First:  "))
            guess2 = int(input("Second: "))

        #guess1=guess2 then make both True (revealed)
        if (discovered[guess1-1]== discovered[guess2-1]):
            discovered[guess1-1]=True
            discovered[guess2-1]=True
            print_boardv2(board,discovered)
            wait_for_player()
            screen_clear()
            #if the cards aren't the same, keep False (hidden)
            if (board[guess1 -1] != board[guess2 -1]):
                discovered[guess1-1]=False
                discovered[guess2-1]=False

        #if guess2 is False and guess1 is True, keep guess2 True (revealed)
        elif (discovered[guess2-1]==False) and (discovered[guess1-1]==True):
            discovered[guess2-1]=True
            print_boardv2(board,discovered)
            wait_for_player()
            screen_clear()
            #unless if they aren't the same card, then keep guess2 False (hidden)
            if (board[guess1 -1] != board[guess2 -1]):
                discovered[guess2-1]=False

        #if guess1 is False and guess2 is True, keep guess1 True (revealed)
        elif (discovered[guess1-1]==False) and (discovered[guess2-1]==True):
            discovered[guess1-1]=True
            print_boardv2(board,discovered)
            wait_for_player()
            screen_clear()
            #unless if they aren't the same card, then keep guess1 False (hidden)
            if (board[guess1 -1] != board[guess2 -1]):
                discovered[guess1-1]=False
               
    print_boardv2(board, discovered)  
    #wait_for_player()   #no   
    #screen_clear()      #no
    best_possible = int(NumbGuesses - (size/2))   
    print("Congratulations! You completed the game with " +str(NumbGuesses)+ " guesses.\nThat is "+str(best_possible)+" more than the best possible.")

def screen_clear():
    '''This function is simply used to clear the screen
    '''
    print("\n"*40)



#this is my own function -other one wasn't adapted to my program
#designing my program by decomposing it into smaller subproblems
#(to be implemented as functions, like this one for my program)
def print_boardv2(a, discovered):
    '''(list of str, discovered)->None
    Prints the current board and in a nicely formated way
    '''
    for i in range(len(a)):
        if discovered[i]==False:
            print('{0:4}'.format("*"), end=' ')
        else:
            print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')
    print()

    
# MAIN 

# YOUR CODE GOES HERE TOO
# HERE YOU OBTAIN THE SIZE OF THE BOARD THE PLAYER WANTS TO PLAY WITH
size=int(input("How many cards do you want to play with?\nEnter an even number between 2 and 52:\n"))

while (size%2==1 or not(size >=2 and size<=52)):
    '''
    when the size is odd or it isn't between 2 and 52
    ask user again until input is valid
    '''
    #print("'Invalid input'")  #NOT necessary but can be helpful to the user in MY program
    size=int(input("How many cards do you want to play with?\nEnter an even number between 2 and 52:\n"))

# this creates the board for you of the given size
board = create_board(size)
# this calls your play_game function that plays the game
play_game(board)
