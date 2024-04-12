# built up a few components needed to build a Tic Tac Toe game in Python:

# Draw the Tic Tac Toe game board
# Checking whether a game board has a winner
# Handle a player move from user input
# The next step is to put all these three components together to make a two-player Tic Tac Toe game! Your challenge in this exercise is to use the functions from those previous exercises all together in the same program to make a two-player game that you can play with a friend

def draw(l):
    n = 3
    print(" ",end="")
    print("--- "*n)
    for i in range(n):
        print("|",end="")
        tem = " {} |"*n
        print(tem.format(numtosym(l[i][0],i,0),numtosym(l[i][1],i,1),numtosym(l[i][2],i,2)))
        print(" ",end="")
        print("--- "*n)
        
def numtosym(n,i,j):
    if n == 0:
        return 3*i + (j+1)
    elif n == 1:
        return "X"
    else:
        return "O"
    
def check(game):
    if( (game[0][0] == game[1][1] and game[0][0] == game[2][2]) or (game[0][2] == game[1][1] and game[0][2] == game[2][0])):
        if(not(game[1][1] == 0)):
            return [1,game[1][1]]
    for i in range(3):
        if game[i][0] == game[i][1] and game[i][0] == game[i][2]:
            if not(game[i][1] == 0):
                return [1,game[i][1]]
        elif game[0][i] == game[1][i] and game[0][i] == game[0][2]:
            if not game[1][i] == 0:
                return [1,game[1][i]]
    return [0]

def usr1(l):
    while(True):
        try:
            u = int(input("Enter the move of user 1 : "))
            if(u>0 and u<10):
                i = u//3
                j = u%3
                j -= 1
                if(u%3 == 0):
                    i -=1
                    j = 2
                if(l[i][j] == 2):
                    print("!!! Position {} already occupied by {}.".format(u,numtosym(l[i][j],i,j)))
                    continue
                l[i][j] = 1
                break
            else:
                print("The move must be between 1 to 9.")
        except:
            print("Enter the correct move")

def usr2(l):
    while(True):
        try:
            u = int(input("Enter the move of user 2 : "))
            if(u>0 and u<10):
                i = u//3
                j = u%3
                j -=1
                if(u%3 == 0):
                    i -=1
                    j = 2
                if(l[i][j] == 1):
                    print("!!! Position {} already occupied by {}.".format(u,numtosym(l[i][j],i,j)))
                    continue
                l[i][j] = 2 
                break
            else:
                print("The move must be between 1 to 9.")
        except:
            print("Enter the correct move")
    
def intro():
    print("\t###########\t WELCOME TO TIC TAC TOE GAME \t #############\n")
    print("\t***************************************************************************\n")
    print("\t***************************************************************************")
    print("\n")

if __name__ == "__main__":
    intro()
    l = [[0,0,0],[0,0,0],[0,0,0]]
    draw(l)
    while(True):
        tem = 0
        
        if(tem != 0):
            break
        else:
            usr1(l)
            draw(l)
            result = check(l)
            if(result[0] != 0):
                break
            usr2(l)
            draw(l)
            result = check(l)
            if(result[0] != 0):
                break
    
    if result[0]:
        if(result[1]==1):
            print("User 1 won the game.")
        else:
            print("User 2 won the game.")
    else:
        print("Draw")
