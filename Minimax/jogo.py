import random


board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

def isvalidPosition(board, position):
    if(board[position[0]][position[1]] == 0):
        return 1
    else:
        return 0


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


def checkLines(board):
    result = 0
    for i in range(3):
        for j in range(3):
            result += board[i][j]

        if (result == 3):
            print("Player fechou a linha ", i)
            return 1  # O player venceu
        elif(result == -3):
            return-1  # O cpu venceu
        else:
            result = 0


def checkCol(board):
    result = 0
    for i in range(3):
        for j in range(3):
            result += board[j][i]

        if (result == 3):
            print("Player fechou a coluna ", i)
            return 1  # O player venceu
        elif(result == -3):
            return-1  # O cpu venceu
        else:
            result = 0


def checkDp(board):
    result = 0
    for i in range(3):
        for j in range(3):
            if(i == j):
                result += board[i][j]

        if result == 3 or result == -3:
            return 1


def checkDs(board):
    result = 0
    for i in range(3):
        for j in range(3):
            if(i + j == 2):
                result += board[i][j]

    if result == 3 or result == -3:
        return 1
 
def randomPosition():
    row = random.randint(0,2)
    col = random.randint(0,2)
    
    arr = [row, col]
    return arr

def isWinner(play):
      if (checkDp(play) or checkDs(play) or checkCol(play) or  checkLines(play)):
          return 1
      else:
        return 0
                   
def getDraw(board):
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
            col = int(input('Insira a coluna que deseja jogar: ')[0])

            position = [row, col]
            
            if(isvalidPosition(board, position)):
            
                play = markPosition(board, position, 1)

                if(isWinner(play)):
                    result = 1
                    
                else:
                    if(getDraw(board)):
                        print("Empate")
                        break
                    else:
                        player = 'cpu'
            
            else:
                print("Posição já preenchida!\n")
                
        else:
            position = randomPosition()
            
            if(isvalidPosition(board,position)):
                play = markPosition(board, position, -1)
                if (isWinner(play)):
                    print("Cpu venceu")
                    result = -1
                    
                else:
                    if(getDraw(board)):
                        print("Empate")
                        break
                    else:
                        player = 'human'

#print()
start()
#randomPosition()
