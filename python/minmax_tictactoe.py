# an implementation for tictactoe AI using minmax and alphabeta pruning
# board is col row array

# boards are always squares
def make_board(xy):
    board = []
    for i in xrange(xy):
        board.append(["_"] * xy)
    return board
        
def print_board(board):
    for i in xrange(len(board)):
        row = [board[j][i] for j in xrange(len(board))]
        print " | ".join(row)
        
def new_state(old, player, (y,x)):
    import copy
    new = copy.deepcopy(old)
    new[y][x] = player
    return new

def game_over(board):
    if get_winner(board) is not None:
        return True

    for col in board:
        for cell in col:
            if cell == "_":
                return False
    return True

def get_winner(board):
    for col in board:
        if len(set(col)) == 1 and col[0] != "_":
            return col[0]
            
    d = len(board)
    rows = [[board[i][x] for i in xrange(d)] for x in xrange(d)]
    for row in rows:
        if len(set(row)) == 1 and row[0] != "_":
            return row[0]
            
    tl_br_diag = [board[i][i] for i in xrange(d)]
    if len(set(tl_br_diag)) == 1 and tl_br_diag[0] != "_":
        return tl_br_diag[0]

    bl_tr_diag = [board[i][j] for (i,j) in zip(reversed(xrange(d)), xrange(d))]
    if len(set(bl_tr_diag)) == 1 and bl_tr_diag[0] != "_":
        return bl_tr_diag[0]
    return None

# does not check that game is actually over
# so might mistake incomplete for draw
def evaluate(board, you):
    win = get_winner(board)
    if win is None:
        return 0
    return 10 if win == you else -10
    
def minmax(board, player="o", opp="x", curr="o", lookAhead=6):
    global ai_move

    if game_over(board) or lookAhead < 0:
        score = evaluate(board, player)
        return (score, None)

    d = len(board)
    moves = [(y,x) for x in xrange(d) for y in xrange(d) if board[y][x] == "_"]
    scores = []
    
    for move in moves:
        next_state = new_state(board, curr, move)
        next = opp if curr == player else player
        score, _ = minmax(next_state, 
                          curr=next,
                          lookAhead=lookAhead - 1)
        scores.append(score)
        
    if curr == player:
        max_score = max(scores)
        ai_move = moves[scores.index(max_score)]
        return (max_score, ai_move)
    else:
        min_score = min(scores)
        return (min_score, None)

board = make_board(3)
# repl to play tictactoe
print "You are X"
print "Enter your moves as: col row"
while(True):
    print
    print "Your Turn: "
    print_board(board)
    input = raw_input()
    y, x = map(int, input.split())
    if board[y][x] != "_":
        print "Invalid move!"
        continue        
    
    board = new_state(board, "x", (y,x))
    print
    print_board(board)
    
    winner = get_winner(board)
    if game_over(board):
        if winner != None:
            if winner == "x":
                print "You win!"
            else:
                print "You lose!"
        else:
            print "Draw!"
        break

    print 
    print "Their turn..."
    
    score, ai_move = minmax(board)
    print ai_move
    board = new_state(board, "o", ai_move)
    print_board(board)

    winner = get_winner(board)
    
    if game_over(board):
        if winner != None:
            if winner == "x":
                print "You win!"
            else:
                print "You lose!"
        else:
            print "Draw!"
        break

