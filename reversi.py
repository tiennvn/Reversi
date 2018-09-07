import random
def createBoard():
    # create a new board with 4 char
    board = [['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', 'W', 'B', '.', '.', '.'],
        ['.', '.', '.', 'B', 'W', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.']]
    return board


def printBoard(inputBoard):
    # print the input Board
    for char in ' abcdefgh':
        print(char.ljust(4), end='')
    i = 1
    for row in inputBoard:
        print('\n')
        print(str(i).ljust(4), end='')
        for col in row:
            print(col.ljust(4), end='')
        i = i + 1
    print('\n')


def changeIn(inChoice):
    # thay doi dau vao tu abcdefgh thanh index 12345678
    inChoice = inChoice.replace('a','1')
    inChoice = inChoice.replace('b','2')
    inChoice = inChoice.replace('c','3')
    inChoice = inChoice.replace('d','4')
    inChoice = inChoice.replace('e','5')
    inChoice = inChoice.replace('f','6')
    inChoice = inChoice.replace('g','7')
    inChoice = inChoice.replace('h','8')
    return inChoice

def playerTurn(player):
    return 'W' if player is 'B' else 'B'


def isOnBoard(x, y):
    # Returns True if on the board
    return x >= 0 and x <= 7 and y >= 0 and y <=7


def isValidMove(board, tile, xstart, ystart):
    # Check valid move
    if board[xstart][ystart] != '.' or not isOnBoard(xstart, ystart):
        return False

    board[xstart][ystart] = tile

    if tile == 'W':
        otherTile = 'B'
    else:
        otherTile = 'W'

    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection
        y += ydirection
        if isOnBoard(x, y) and board[x][y] == otherTile:
            x += xdirection
            y += ydirection
            if not isOnBoard(x, y):
                continue
            while board[x][y] == otherTile:
                x += xdirection
                y += ydirection
                if not isOnBoard(x, y):
                    break
            if not isOnBoard(x, y):
                continue
            if board[x][y] == tile:
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])

    board[xstart][ystart] = '.'
    if len(tilesToFlip) == 0:
        return False
    return tilesToFlip


def validChoice(validPlace):
    for place in validPlace:
            print("x= ", place[1] + 1, "y= ", place[0] + 1, end=' | ')


def makeMove(board, tile, xstart, ystart):
    hereFlip = isValidMove(board, tile, xstart, ystart)
    board[xstart][ystart] = tile
    for x,y in hereFlip:
        board[x][y] = tile
    return board


def getScoreBoard(board):
    Wpoint, Bpoint = 0, 0
    for row in board:
        for element in row:
            if element == B:
                Bpoint += 1
            if element == W:
                Wpoint += 1
    return {B:Bpoint, W:Wpoint}


def main():
    B = 'B'
    W = 'W'
    EMPTY = '.'

    mainBoard = createBoard() # Tao bang
    turn = W
    done = 0
    while done != 2:
        printBoard(mainBoard) # In bang
        turn = playerTurn(turn) # luot danh cua player

        ## In ra valid choice
        validPlace = []
        for x in range(8):
            for y in range(8):
                if isValidMove(mainBoard,turn, x, y) != False:
                    validPlace.append([x,y])
        print("validPlace", validPlace)
        if validPlace == []:
            print('Player', turn, 'cannot play.')
            done += 1
            print(input())
        else:
            done = 0

        print("Valid choices:" , validPlace) # in ra valid choices
        print(validChoice(validPlace))

        ## Luot danh cua player
        print("Player " + turn + ":")
        # inputChoice = input("x,y: ")
        if validPlace != []:
            [x,y] = random.choice(validPlace)
            print(x,y)
            mainBoard = makeMove(mainBoard, turn, x, y)
        else:
            pass
        # x = int(inputChoice[0])
        # y = int(inputChoice[1])

        ## thuc hien lua chon


    print("End of the game. W: ", getScoreBoard(mainBoard)[W], ", B: ", getScoreBoard(mainBoard)[B])

if __name__ == "__main__":
    main()
