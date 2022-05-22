from emoji import emojize
from evaluation.evaluation import evaluate

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

def isMovesLeft(board):
    for i in range(3):
        for j in range(3):
           if (board[i][j] == 0) :
                return True
    return False

def isvalidPosition(board, position):
    if(board[position[0]][position[1]] == 0):
        return True
    else:
        return False

def markPosition(board, position, marker):

    if(isvalidPosition(board, position)):
        board[position[0]][position[1]] = marker
        printBoard(board)
        print('\n')
        return board


def printBoard(board):
    for i in range(3):
        for j in range(3):
            print(" [", board[i][j], "] ", end='')
        print('')
       
 
def minimax(board, depth, isMax):
    result = evaluate(board)

    if(result == 3):
        return result

    if (result == -3) :
        return result

    if (isMovesLeft(board) == False) :
        return 0
    
    if (isMax) :    
        best = -300
        for i in range(3) :        
            for j in range(3) :
                if (board[i][j]==0) :
                    board[i][j] = 1
                    best = max( best, minimax(board,depth + 1, not isMax) )
                    board[i][j] = 0
        return best
    
    else:
        best = 300
        for i in range(3) :        
            for j in range(3) :
                if (board[i][j] == 0) :
                    board[i][j] = -1
                    best = min(best, minimax(board, depth + 1, not isMax))                    
                    board[i][j] = 0
        return best
    
def findBestMove(board) :
    bestVal = -300
    bestMove = (-1, -1)
 
    for i in range(3) :    
        for j in range(3) :
         
             if (board[i][j] == 0) :
             
                board[i][j] = 1
                
                moveVal = minimax(board, 0, False)
                
                board[i][j] = 0
 
                if (moveVal > bestVal) :               
                    bestMove = (i, j)
                    bestVal = moveVal
    return bestMove
 
def iA():
    bestMove = findBestMove(board)
    arr = [bestMove[0], bestMove[1]]
    return arr
 
                   
def getTie(board):
    for i in range(3):
        for j in range(3):
            if(board[i][j] == 0):
                return 0
    return 1
    
def start():
    result = 0
    player = 'human'
    while (result == 0):
        
        if (player == 'human'):
            
            row = int(input('Insira a linha que deseja jogar: ')[0])
            col = int(input('Insira a coluna que deseja jogar: \n')[0])

            position = [row, col]
            
            if(isvalidPosition(board, position)):
            
                play = markPosition(board, position, -1)

                if(evaluate(play) == -3):
                    result = -1
                    
                else:
                    if(getTie(board)):
                        print(emojize("Já era! O jogo empatou :hot_face:", use_aliases=True))
                        break
                    else:
                        player = 'cpu'
            
            else:
                print("Posição já preenchida!\n")
                
        else:
            position = iA()
            
            if(isvalidPosition(board,position)):
                
                print(emojize(":robot: CPU jogou: \n", use_aliases=True))
                play = markPosition(board, position, 1)
                if (evaluate(play) == 3):
                    print(emojize(":trophy: CPU venceu", use_aliases=True))
                    result = 1
                    
                else:
                    if(getTie(board)):
                        print(emojize("Já era! O jogo empatou :hot_face:", use_aliases=True))
                        break
                    else:
                        player = 'human'
start()