#a function that generate a raw
def gen_row(i):
    row = []
    for j in range(0,8):
        row.append(i)
        i += 1
    return row
    
    

#a function that generate a column
def gen_column(i):
    column = []
    for j in range(0,8):
        column.append(i)
        i += 8
    return column
    
    
#a function that generate a chessboard:
def gen_board():
    board = []
    r = 0
    for i in range(0,8):
            board.append(gen_row(r))
            r = r + 8 
    return board   

#i see the board cells like graphs, and the possibile moves like edge


#a funciton that generate all possibile moves from a position
def gen_moves(cell):
    moves = []
    handler = []
    #Case when the knight have less moves cause y
    lymm = gen_row(0)
    lym = gen_row(8)
    lyp = gen_row(48)
    lypp = gen_row(56)
    #Case when the knight have less moves cause x
    lxmm = gen_column(0)
    lxm = gen_column(1)
    lxp = gen_column(6)
    lxpp = gen_column(7)
    moves_x = [-2,-1,1,2]
    moves_y = [-16,-8,8,16]


    if cell in lypp:
        moves_y.remove(16)
        moves_y.remove(8)
    
    if cell in lyp:
        moves_y.remove(16)

    if cell in lymm:
        moves_y.remove(-16)
        moves_y.remove(-8)
        
    if cell in lym:
        moves_y.remove(-16)
      
    if cell in lxpp:
        moves_x.remove(2)
        moves_x.remove(1)
        
    if cell in lxp:
        moves_x.remove(2) 
        
    if cell in lxmm:
        moves_x.remove(-2) 
        moves_x.remove(-1)
        
    if cell in lxm:
        moves_x.remove(-2) 
        
    for x in moves_x:
        for y in moves_y:
            if ((abs(y) == 16 and abs(x) == 1) or (abs(y) == 8 and abs(x) == 2)):
                handler.append([x,y])


    
    for m in handler:
        moves.append(cell + m[0] + m[1])

    return moves
    
    
def goal_mask():
    goal = []
    for i in range (0,64):
            goal.append(0)
    return goal
    
    
def mask_filler(moves, mask):
    for m in moves:
        mask[m] = 1
    return mask
    
        
def mask_checker(current_list, goal):
        for num in current_list:
            if goal[num] == 1:
                return True
    
    
def solution(src,dest):
    
    #remove case src == dst
    if (src == dest):
        return 0

    goal = goal_mask()
    counter = 0
    src_list = []
    dest_list = []
    current_list_src = []
    current_list_dst = []
    
    
    #Starting two steps of "BFS" from dest to to fill the mask
    #if the source is already found it returns the number of steps
    
    current_list_dst = gen_moves(dest)
    counter += 1
    
    if src in current_list_dst:
        return counter
    else:
        goal = mask_filler(current_list_dst,goal)
        
    for k in current_list_dst:
        moves = gen_moves(k)
        for ma in moves:
            dest_list.append(ma)
    
    counter += 1
    
    
    if mask_checker(dest_list,goal):
        return counter
    else:
        goal = mask_filler(dest_list,goal)
            
    
    #Starting BFS from SRC, every time I check in the mask 
    #if i reach the dest
    
    current_list_src = gen_moves(src)
    counter += 1
    
    if mask_checker(current_list_src,goal):
        return counter

 
    #Worst case scenario in BFS
    for kk in range(0,5):
        
    
        for k in current_list_src:
            moves = gen_moves(k)
            for ma in moves:
                #if ma not in src_list:
                src_list.append(ma)
    
        counter += 1

        if mask_checker(src_list,goal):
            return counter
        else:
            current_list_src = src_list
            src_list = []