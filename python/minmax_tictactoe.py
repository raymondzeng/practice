# an implementation for tictactoe AI using minmax and alphabeta pruning
# board is y x array

# boards are always squares
def make_board(xy):
    board = []
    for i in xrange(xy):
        board.append(["_"] * xy)
    return board
        
def print_board(board):
    for col in board:
        print " | ".join(col)            

def new_state(old, player, (x,y)):
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
            
    diag = [board[i][i] for i in xrange(len(board))]
    if len(set(diag)) == 1 and diag[0] != "_":
        return diag[0]

    return None

# does not check that game is actually over
# so might mistake incomplete for draw
def score(board, you):
    win = get_winner(board)
    if win is None:
        return 0
    return 10 if win == you else -10
    
ai_move = None
def minmax(board, player="o", opp="x", curr_player="o"):
    global ai_move
    if game_over(board):
        return score(board, player)

    d = len(board)
    moves = [(x,y) for x in xrange(d) for y in xrange(d) if board[y][x] == "_"]
    scores = []
    
    for move in moves:
        next_state = new_state(board, curr_player, move)
        next_turn = opp if curr_player == player else player
        scores.append((minmax(next_state, player, opp, next_turn)))

    if curr_player == player:
        max_score = max(scores)
        ai_move = moves[scores.index(max_score)]
        return max_score
    else:
        min_score = min(scores)
        ai_move = moves[scores.index(min_score)]
        return min_score

board = make_board(3)
print "You are X"
print "Enter your moves as: x y"
while(True):
    print
    print "Your Turn: "
    print_board(board)
    input = raw_input()
    x, y = map(int, input.split())
    if board[y][x] != "_":
        print "Invalid move!"
        continue

    board = new_state(board, "x", (x,y))
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
    
    minmax(board)
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


    

#### TODO : still incorrect! AI didn't block me when I was about to win
# to recreate bug:
# 0 2 -> 1 1
