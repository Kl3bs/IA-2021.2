def evaluate(board):
 
    line_value = 0
    for i in range(3):
        for j in range(3):
            line_value += board[i][j]

        if (line_value == 3):
             return 3  # O player venceu
        elif(line_value == -3):
            return -3  # O cpu venceu
        line_value = 0
        
    col_value = 0
    for i in range(3):
        for j in range(3):
            col_value += board[j][i]

        if (col_value == 3):
            return 3  # O player venceu
        elif(col_value == -3):
            return -3  # O cpu venceu
        col_value = 0
 
    dp_value = 0
    for i in range(3):
        for j in range(3):
            if(i == j):
                dp_value += board[i][j]

        if dp_value == 3:
            return 3
        elif dp_value == -3:
            return -3
        
        
    ds_value = 0
    for i in range(3):
        for j in range(3):
            if(i + j == 2):
                ds_value  += board[i][j]

        if ds_value  == 3:
                return 3
        elif ds_value  == -3:
            return -3
 
 