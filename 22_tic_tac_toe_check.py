# Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.

# If a game of Tic Tac Toe is represented as a list of lists, like so:

# game = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]
# where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.

# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.

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

if __name__ == "__main__":
    result = check([[1, 2, 2],
                    [2, 1, 0],
                    [2, 1, 1]])
    if result[0]:
        if(result[1]==1):
            print("User 1 won the game.")
        else:
            print("User 2 won the game.")
    else:
        print("Draw")