#board 

board = [
    ' ', ' ', ' ', 
    ' ', ' ', ' ',
    ' ', ' ', ' ']

Player = "X"
winner = None
gameRunning = True

#input player
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-" * 9)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-" * 9)
    print(board[6] + " | " + board[7] + " | " + board[8])

def playerInput(board):
    num = int(input('Enter a number between 1-9: '))
    
    if num >= 1 and num <= 9 and board[num-1] == ' ':
        board[num-1] = Player
    else:
        print("It's already taken!")
        
#check kung win or tie
def checkHoriTie(board):
    global winner 
    if board [0] == board [1] == board [2] and board [1] != ' ':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != ' ':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != ' ':
        winner = board [6]
        return True
    
def checkColumn(board):
    global winner 
    if board[0] == board[3] == board[6] and board[0] != ' ':
        winner = board [0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != ' ':
        winner = board [1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != ' ':
        winner = board[2]
        return True
        
def checkDiaTie(board):
    global winner
    if board[0] == board[4] == board[8] and board[4] != ' ':
        winner = board[0]
        return True
    elif board[6] == board[4] == board[2] and board[6] != ' ':
        winner == board[6]
        return True
    
def checkTie(board):
    global gameRunning
    if ' ' not in board:
        printBoard(board)
        print("It's a tie!")
        gameRunning = False


#check for win
def checkWin(board):
    if checkDiaTie(board) or checkHoriTie(board) or checkColumn (board):
        print(f"The winner is {winner}")
#switch player

def switchPlayer(): 
    global Player
    if Player == "X":
      Player = "O"
    else:
        Player = "X"

#check for win or tie ulit

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin(board)
    checkTie(board)
    switchPlayer()
