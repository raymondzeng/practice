def exist(board, word):
    starting = [(i, j) for i, l in enumerate(board) for j, s in enumerate(l) if board[i][j] == word[0]]
    
    for coord in starting:
        if found(word[1:], coord, board, [coord]):
            return True
    return False

def found(word, start, board, seen):
    print word, start, seen
    if len(word) == 0:
        return True

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    x, y = start

    for i in xrange(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (nx,ny) in seen or nx < 0 or ny < 0:
            continue

        try:
            el = board[nx][ny]
            if el == word[0]:
                seen.append((nx,ny))
                if found(word[1:], (nx, ny), board, seen):
                    return True
            continue
        except:
            continue
    return False



# assert(exist(["ABCD", 
#               "HIJK", 
#               "LIKIA"], "ABCDKJI") == True)
# assert(exist(["ABCD", 
#               "HIJK", 
#               "LIKIA"], "ABCDKDC") == False)

# assert(exist(["AA"], "AAA") == False)
# assert(exist(["AB"], "AB") == True)

# assert(exist(["CCC",
#               "AAA",
#               "BCD"], "AAB") == True)

assert(exist(["ABCE",
              "SFES",
              "KDEE"], "ABCESEEEFS") == True)
