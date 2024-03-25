# For this exercise, assume that player 1 (the first player to move) will always be X and player 2 (the second player) will always be O.
# Notice how in the example I gave coordinates for where I want to move starting from (1, 1) instead of (0, 0). To people who don’t program, starting to count at 0 is a strange concept, so it is better for the user experience if the row counts and column counts start at 1. This is not required, but whichever way you choose to implement this, it should be explained to the player.
# Ask the user to enter coordinates in the form “row,col” - a number, then a comma, then a number. Then you can use your Python skills to figure out which row and column they want their piece to be in.
# Don’t worry about checking whether someone won the game, but if a player tries to put a piece in a game position where there already is another piece, do not allow the piece to go there.

def draw(l):
    n = 3
    print(" ",end="")
    print("--- "*n)
    for i in range(n):
        print("|",end="")
        tem = " {} |"*n
        print(tem.format(numtosym(l[i][0]),numtosym(l[i][1]),numtosym(l[i][2])))
        print(" ",end="")
        print("--- "*n)

def numtosym(n):
    if n == 0:
        return " "
    elif n == 1:
        return "X"
    else:
        return "0"

if __name__ == "__main__":
    l = [[1, 2, 2],
                    [2, 1, 0],
                    [2, 1, 1]]
    draw(l)