# an implementation for tictactoe AI using minmax and alphabeta pruning
# board array access is board[col][row]

# boards are always squares
def make_board(width):
    board = []
    for i in xrange(width):
        board.append(["_"] * width)
    return board
        
# board is a list of columns and we want to print by row
def print_board(board):
    for i in xrange(len(board)):
        row = [board[j][i] for j in xrange(len(board))]
        print " | ".join(row)
        
# create a new board but with position @(col, row) changed to @player
def new_state(old, player, (col,row)):
    import copy
    new = copy.deepcopy(old)
    new[col][row] = player
    return new

def get_winner(board):
    # look for vertical win
    for col in board:
        if len(set(col)) == 1 and col[0] != "_":
            return col[0]
            
    # horizontal win
    d = len(board)
    rows = [[board[i][x] for i in xrange(d)] for x in xrange(d)]
    for row in rows:
        if len(set(row)) == 1 and row[0] != "_":
            return row[0]
            
    # diagonal win: top left to bottom right
    tl_br_diag = [board[i][i] for i in xrange(d)]
    if len(set(tl_br_diag)) == 1 and tl_br_diag[0] != "_":
        return tl_br_diag[0]

    # bottom left to top right
    bl_tr_diag = [board[i][j] for (i,j) in zip(reversed(xrange(d)), xrange(d))]
    if len(set(bl_tr_diag)) == 1 and bl_tr_diag[0] != "_":
        return bl_tr_diag[0]
    
    # no winner
    return None

def game_over(board):
    if get_winner(board) is not None:
        return True

    for col in board:
        for cell in col:
            if cell == "_":
                return False
    return True

# returns 10 if @you is the winner, -10 if @you is the loser
# and 0 otherwise (tie, or game not over)
def evaluate(board, you):
    win = get_winner(board)
    if win is None:
        return 0
    return 10 if win == you else -10
    
def minmax(board, player="o", opp="x", curr="o", depth=9, alpha=-20, beta=20):
    if game_over(board) or depth < 0:
        score = evaluate(board, player)
        return (score, None)

    d = len(board)
    moves = [(y,x) for y in xrange(d) for x in xrange(d) if board[y][x] == "_"]
    
    move_to_return = None
    for move in moves:
        next_state = new_state(board, curr, move)
        score, _ = minmax(next_state, 
                          curr=opp if curr == player else player,
                          depth= depth - 1,
                          alpha=alpha, 
                          beta=beta)

        # alpha beta pruning
        if curr == player:
            if score > alpha:
                alpha = score
                move_to_return = move
            if alpha >= beta:
                break
        else:
            if score < beta:
                beta = score
            if alpha >= beta:
                break
    
    # return either max or min, respectively
    if curr == player:
        return (alpha, move_to_return)
    else:
        return (beta, None)
                


#repl to play tictactoe against AI
board = make_board(3)
board[0][2] = "x"
board[0][0] = "o"
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

