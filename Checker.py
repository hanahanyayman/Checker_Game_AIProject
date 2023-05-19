import random

Board=[
      [ 0 ,'R', 0 ,'R', 0 ,'R', 0 ,'R'],
      ['R', 0 ,'R', 0 ,'R', 0 ,'R', 0 ],
      [ 0 ,'R', 0 ,'R', 0 ,'R', 0 ,'R'],
      ['-', 0 ,'-', 0 ,'-', 0 ,'-', 0 ],
      [ 0 ,'-', 0 ,'-', 0 ,'-', 0 ,'-'],
      ['B', 0 ,'B', 0 ,'B', 0 ,'B', 0 ],
      [ 0 ,'B', 0 ,'B', 0 ,'B', 0 ,'B'],
      ['B', 0 ,'B', 0 ,'B', 0 ,'B', 0 ]
     ]


'''Board=[
      [ 0 ,'-', 0 ,'-', 0 ,'-', 0 ,'-'],
      ['-', 0 ,'-', 0 ,'-', 0 ,'-', 0 ],
      [ 0 ,'-', 0 ,'-', 0 ,'KR', 0 ,'-'],
      ['-', 0 ,'-', 0 ,'-', 0 ,'-', 0 ],
      [ 0 ,'-', 0 ,'-', 0 ,'-', 0 ,'-'],
      ['-', 0 ,'KB', 0 ,'-', 0 ,'-', 0 ],
      [ 0 ,'-', 0 ,'-', 0 ,'-', 0 ,'-'],
      ['-', 0 ,'-', 0 ,'-', 0 ,'-', 0 ]
     ]'''

depth=None

def return_board(board):
    tempboard=[[],[],[],[],[],[],[],[]]
    for i in range(0,8):
        for j in range(0,8):
           tempboard[i].append(board[i][j])
    return tempboard

def Assign(board):
    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            Board[i][j]=board[i][j]

def convert_to_king(board,i,j):
    tempboard=return_board(board)
    if i == 0 and tempboard[i][j] == 'B':
        tempboard[i][j]='KB'
    elif i == 7 and tempboard[i][j] == 'R':
        tempboard[i][j]='KR'
    return tempboard

def return_with_new_move(board,i,j,x,y):
    tempboard=return_board(board)
    tempboard[x][y]=tempboard[i][j]
    tempboard[i][j]='-'
    return tempboard

def return_with_new_move_beat(board,i,j,a,b,x,y):
    tempboard=return_board(board)
    tempboard[x][y]=tempboard[i][j]
    tempboard[i][j]='-'
    tempboard[a][b]='-'
    return tempboard

def move_R(board,i,j):
    Children=[]
    if j > 0 and i < 7 and  board[i+1][j-1]  == '-':
        tempboard=return_with_new_move(board,i,j,i+1,j-1)
        tempboard=convert_to_king(tempboard,i+1,j-1)
        if tempboard != board:
           Children.append(tempboard)
    if j < 7 and i < 7 and   board[i+1][j+1] == '-':
        tempboard=return_with_new_move(board,i,j,i+1,j+1)
        tempboard=convert_to_king(tempboard,i+1,j+1)
        if tempboard != board:
           Children.append(tempboard)
    return Children

def move_and_beat_R(board,i,j):
    if board[i][j] == 'R' or board[i][j] == 'KR':
       Enemy1='B'
       Enemy2='KB'
    else:
        Enemy1='R'
        Enemy2='KR'
    Children=[]
    flag=True
    tempboard=return_board(board)
    a=i
    b=j
    while flag:
     flag=False
     if b < 6 and a < 6 and (tempboard[a+1][b+1] ==Enemy1 or tempboard[a+1][b+1] == Enemy2) and tempboard[a+2][b+2] == '-':
        tempboard=return_with_new_move_beat(tempboard,a,b,a+1,b+1,a+2,b+2)
        tempboard=convert_to_king(tempboard,a+2,b+2)
        flag=True
        a=a+2
        b=b+2
    if tempboard != board:
       Children.append(tempboard)
    tempboard=return_board(board)
    flag=True
    a=i
    b=j
    while flag:
     flag=False
     if b > 1 and a < 6 and (tempboard[a+1][b-1] == Enemy1 or tempboard[a+1][b-1] == Enemy2 )and tempboard[a+2][b-2]  == '-':
        tempboard=return_with_new_move_beat(tempboard,a,b,a+1,b-1,a+2,b-2)
        tempboard=convert_to_king(tempboard,a+2,b-2)
        flag=True
        a=a+2
        b=b-2
    if tempboard != board:
       Children.append(tempboard)
    return Children

def move_B(board,i,j):
    Children=[]
    if j > 0 and i > 0 and  board[i-1][j-1]  == '-':
        tempboard=return_with_new_move(board,i,j,i-1,j-1)
        tempboard=convert_to_king(tempboard,i-1,j-1)
        if tempboard != board:
           Children.append(tempboard)
    if j < 7 and i > 0 and   board[i-1][j+1] == '-':
        tempboard=return_with_new_move(board,i,j,i-1,j+1)
        tempboard=convert_to_king(tempboard,i-1,j+1)
        if tempboard != board:
           Children.append(tempboard)
    return Children

def move_and_beat_B(board,i,j):
    if board[i][j] == 'R' or board[i][j] == 'KR':
       Enemy1='B'
       Enemy2='KB'
    else:
        Enemy1='R'
        Enemy2='KR'
    Children=[]
    flag=True
    tempboard=return_board(board)
    a=i
    b=j
    while flag:
      flag=False
      if b > 1 and a > 1 and (tempboard[a-1][b-1] ==Enemy1 or tempboard[a-1][b-1] == Enemy2 ) and tempboard[a-2][b-2]  == '-':
        tempboard=return_with_new_move_beat(tempboard,a,b,a-1,b-1,a-2,b-2)
        tempboard=convert_to_king(tempboard,a-2,b-2)
        flag=True
        a=a-2
        b=b-2
    if tempboard != board:
       Children.append(tempboard)
    tempboard=return_board(board)
    flag=True
    a=i
    b=j
    while flag:
      flag =False
      if b < 6 and a > 1 and  (tempboard[a-1][b+1] == Enemy1 or tempboard[a-1][b+1] == Enemy2 ) and tempboard[a-2][b+2] == '-':
        tempboard=return_with_new_move_beat(tempboard,a,b,a-1,b+1,a-2,b+2)
        tempboard=convert_to_king(tempboard,a-2,b+2)
        flag=True
        a=a-2
        b=b+2
    if tempboard != board:
       Children.append(tempboard)
    return Children

def get_all_children_R(board):
    Children=[]
    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            if board[i][j] == 'R':
                temp=move_R(board,i,j)
                for x in range(0, len(temp)):
                    Children.append(temp[x])
                temp=move_and_beat_R(board,i,j)
                for x in range(0, len(temp)):
                    Children.append(temp[x])
            elif board[i][j] == 'KR':
                temp=move_R(board,i,j)
                for x in range(0, len(temp)):
                    Children.append(temp[x])
                temp=move_and_beat_R(board,i,j)
                for x in range(0, len(temp)):
                    Children.append(temp[x])
                temp=move_B(board,i,j)
                for x in range(0, len(temp)):
                    Children.append(temp[x])
                temp=move_and_beat_B(board,i,j)
                for x in range(0, len(temp)):
                    Children.append(temp[x])
    return Children

def get_all_children_B(board):
    Children=[]
    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            if board[i][j] == 'B':
                temp=move_B(board,i,j)
                for x in range(0, len(temp)):
                    Children.append(temp[x])
                temp=move_and_beat_B(board,i,j)
                for x in range(0, len(temp)):
                    Children.append(temp[x])
            elif board[i][j] == 'KB':
                temp=move_R(board,i,j)
                for x in range(0, len(temp)):
                    Children.append(temp[x])
                temp=move_and_beat_R(board,i,j)
                for x in range(0, len(temp)):
                    Children.append(temp[x])
                temp=move_B(board,i,j)
                for x in range(0, len(temp)):
                    Children.append(temp[x])
                temp=move_and_beat_B(board,i,j)
                for x in range(0, len(temp)):
                    Children.append(temp[x])
    return Children

def print_grid(grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 0 :
                    print(" # ", end="\t")
                elif grid[i][j] == '-':
                    print("   ", end="\t")
                elif grid[i][j] == 'R':
                    print(" R ", end="\t")
                elif grid[i][j] == 'B':
                    print(" B ", end="\t")
                elif grid[i][j] == 'KB':
                    print(" KB ", end="\t")
                elif grid[i][j] == 'KR':
                    print(" KR ", end="\t")
            print("\n")

def Winner(board):
    LossR=True
    LossB=True
    for i in range (0,len(board)):
        for j in range(0,len(board[i])):
            if board[i][j] == 'R' or board[i][j] == 'KR':
                LossR=False
                break
    for i in range (0,len(board)):
        for j in range(0,len(board[i])):
            if board[i][j] == 'B' or board[i][j] == 'KB':
                LossB=False
                break
    if LossB and not LossR:
        return 'R'
    elif LossR and not LossB:
        return 'B'
    return 0

def utility(board,Player):
    if Player == 'R':
        oppo='B'
    else:
        oppo='R'
    Win = Winner(board)
    if Win == oppo:
        return -20
    elif Win == Player:
        return 20
    return 0

def calculate(board,Player):
    if Player == 'R':
        king='KR'
        kingoppo='KB'
        oppo='B'
    else:
        king='KB'
        kingoppo='KR'
        oppo='R'
    NumCurrentPlayer = 0
    NumOtherPlayer = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == Player  or board[i][j] == king:
                NumCurrentPlayer = NumCurrentPlayer + 1
            elif board[i][j] == oppo or board[i][j] == kingoppo:
                NumOtherPlayer = NumOtherPlayer + 1
    if NumCurrentPlayer == NumOtherPlayer :
        return 0
    return NumCurrentPlayer - NumOtherPlayer

def minmax(board,Depth,Player):
    list_children_same_max=[]
    if Player == 'B':
        PrivousPlayer='R'
        Children=get_all_children_B(board)
    else:
        PrivousPlayer='B'
        Children=get_all_children_R(board)

    if utility(board,PrivousPlayer) != 0:
       return utility(board,PrivousPlayer)
   
    if Children == []:
       return 0
   
    if Depth == 0:
       return calculate(board,PrivousPlayer)
    
    if Player == 'B':
      value=-10000000000000000
      for i in range(0,len(Children)):
        max_value_of_children=minmax(Children[i],Depth-1,'R')
        if  value < max_value_of_children:
            value = max_value_of_children
            list_children_same_max=[]
            list_children_same_max.append(Children[i])
        elif value == max_value_of_children:
            list_children_same_max.append(Children[i])
    else:
      value=10000000000000000
      for i in range(0,len(Children)):
        min_value_of_children=minmax(Children[i],Depth-1,'B')
        if value > min_value_of_children:
            value = min_value_of_children
       

    if depth == Depth:
        print(value)
        if list_children_same_max == []:
            return None
        else:    
            return list_children_same_max[random.randint(0,len(list_children_same_max)-1)]
    else:
        return value

def get_child_by_random(board,NextPlayer):
    Children=None
    if NextPlayer == 'R':
       Children=get_all_children_R(board)
    else:
       Children=get_all_children_B(board)
    if Children == []:
        return []
    child=random.randint(0,len(Children)-1)
    return Children[child] 

if __name__ == "__main__":
    tempboard=Board
    depth=3

    while utility(tempboard,'R') == 0 and tempboard != None:
        print("Computer plays ...")
        tempboard = minmax(tempboard,depth,'B')
        if tempboard != []:
           Assign(tempboard)
           print_grid(tempboard)
        else:
            break
        print("----------------------------")
        if utility(tempboard,'B') == 0 and tempboard != None:
            print("AI plays ...")
            tempboard = get_child_by_random(tempboard,'R')
            if tempboard != None:
               Assign(tempboard)
               print_grid(tempboard)
            else:
                break
            print("----------------------------")

    if tempboard == None:
        print("Draw")
    elif utility(tempboard,'B') == 20:
        print("AI wins")
    else:
        print("Computer wins")