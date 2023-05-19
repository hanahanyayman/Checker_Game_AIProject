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
NextPlayer='B'
Num=0
class State:
    BoardState=None
    NextState=None
    Number=None
    Player=None


def convert_to_king(board,i,j):
    tempboard=return_board(board)
    if i == 0 and tempboard[i][j] == 'B':
        tempboard[i][j]='KB'
    elif i == 7 and tempboard[i][j] == 'R':
        tempboard[i][j]='KR'
    return tempboard

def get_child_by_random(board):
    if NextPlayer == 'R':
       Children=get_all_children_R(board)
    else:
       Children=get_all_children_B(board)
    child=random.randint(0,len(Children)-1)
    return Children[child]

def return_board(board):
    tempboard=[[],[],[],[],[],[],[],[]]
    for i in range(0,8):
        for j in range(0,8):
           tempboard[i].append(board[i][j])
    return tempboard

def return_with_new_move(board,i,j,x,y):
    tempboard=return_board(board)
    temp=tempboard[i][j]
    tempboard[i][j]=tempboard[x][y]
    tempboard[x][y]=temp
    return tempboard

def return_with_new_move_beat(board,i,j,a,b,x,y):
    tempboard=return_board(board)
    temp=tempboard[i][j]
    tempboard[i][j]='-'
    tempboard[x][y]=temp
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

def print_grid(grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 0 :
                    print("0", end=" \t")
                elif grid[i][j] == '-':
                    print("-", end=" \t")
                elif grid[i][j] == 'R':
                    print("R", end=" \t")
                elif grid[i][j] == 'B':
                    print("B", end=" \t")
                elif grid[i][j] == 'KB':
                    print("KB", end=" \t")
                elif grid[i][j] == 'KR':
                    print("KR", end=" \t")
            print("\n")

def utility(board):
    Win=Winner(board)
    if Win == 'R':
        return -1
    elif Win == 'B':
        return 1
    return 0

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
    return 'N'

    pass

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

def minmax(board,depth):
   global NextPlayer
   global Num
   state=State()
   state.BoardState=board
   state.Number=Num
   state.NextState=[]
   state.Player=NextPlayer
   Children=[]
   NextBoard=None
   if depth == 0:
       return 0
   
   if NextPlayer == 'B':
      Children=get_all_children_B(state.BoardState)
   else:
      Children=get_all_children_R(state.BoardState)

   if utility(state.BoardState) != 0:
       return utility(state.BoardState)
   
   if Children == []:
       return 0
   
   if state.Player == 'R':
           NextPlayer='B'
           Num=-10000000000000000000000
   else:
           NextPlayer='R'
           Num=10000000000000000000000

   for i in range(0,len(Children)):
       num=minmax(Children[i],depth-1)
       if state.Player == 'B' and state.Number <= num:
           state.Number=num
           NextBoard=Children[i]
       elif state.Player == 'R' and state.Number > num:
           state.Number=num
   if state.BoardState == Board:
       return NextBoard
   else:
       return num
    
if __name__ == "__main__":
   pass