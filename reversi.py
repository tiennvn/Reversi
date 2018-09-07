import random


def createBoard():
    # Create a new board with 4 char
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
    # Print the board
    for char in ' a b c d e f g h':
        print(char, end='')
    i = 1
    for row in inputBoard:
        print('\n')
        print(str(i), '', end='')
        for col in row:
            print(col, '', end='')
        i = i + 1
    print('\n')


def playerTurn(player):
    return 'W' if player is 'B' else 'B'


def isOnBoard(x, y):
    # Returns True if on the board
    return x >= 0 and x <= 7 and y >= 0 and y <=7


def isOnBoard(y, x):
        # Returns True if the coordinates are located on the board.
        return x >= 0 and x <= 7 and y >= 0 and y < 7


def isValidMove(board, tile, ystart, xstart):
    if board[ystart][xstart] != '.' or not isOnBoard(ystart, xstart):
        return False
    board[ystart][xstart] = tile
    if tile == 'W':
        otherTile = 'B'
    else:
        otherTile = 'W'
    tilesToFlip = []
    for ydirection, xdirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1],
                                   [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection
        y += ydirection
        if isOnBoard(y, x) and board[y][x] == otherTile:
            x += xdirection
            y += ydirection
            if not isOnBoard(y, x):
                continue
            while board[y][x] == otherTile:
                x += xdirection
                y += ydirection
                if not isOnBoard(y, x):
                    break
            if not isOnBoard(y, x):
                continue
            if board[y][x] == tile:
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([y, x])
    board[ystart][xstart] = '.'
    if len(tilesToFlip) == 0:
        return False
    return tilesToFlip


def validChoice(validPlace):
    validInput = []
    for place in validPlace:
        print(toStr(place[1], place[0] + 1), end=' ')
        validInput.append(toStr(place[1], place[0] + 1))
    return validInput


def makeMove(board, tile, ystart, xstart):
    hereFlip = isValidMove(board, tile, ystart, xstart)
    board[ystart][xstart] = tile
    for y, x in hereFlip:
        board[y][x] = tile
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


def strToInt(string):
    string = string.replace('a', '1')
    string = string.replace('b', '2')
    string = string.replace('c', '3')
    string = string.replace('d', '4')
    string = string.replace('e', '5')
    string = string.replace('f', '6')
    string = string.replace('g', '7')
    string = string.replace('h', '8')
    x = int(string[1]) - 1
    y = int(string[0]) - 1
    return [x, y]


def toStr(x, y):
    intToStr = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
    result = intToStr[x] + str(y)
    return result


def changeIn(inChoice):
    # thay doi dau vao tu abcdefgh thanh index 12345678
    inChoice = inChoice.replace('a', '1')
    inChoice = inChoice.replace('b', '2')
    inChoice = inChoice.replace('c', '3')
    inChoice = inChoice.replace('d', '4')
    inChoice = inChoice.replace('e', '5')
    inChoice = inChoice.replace('f', '6')
    inChoice = inChoice.replace('g', '7')
    inChoice = inChoice.replace('h', '8')
    return inChoice


def main():
    B = 'B'
    W = 'W'
    mainBoard = createBoard()
    turn = W
    done = 0
    while done != 2:
        printBoard(mainBoard)
        turn = playerTurn(turn)
        validPlace = []
        outputValidPlace = []
        for y in range(8):
            for x in range(8):
                if isValidMove(mainBoard, turn, x, y) is not False:
                    validPlace.append([x, y])
                    outputValidPlace.append(toStr(x, y))
        if validPlace == []:
            print('Player', turn, 'cannot play.')
            done += 1
        else:
            done = 0
        print("Valid choices: \n", end='')
        validInput = validChoice(validPlace)
        print("Player " + turn + ":", end='')

        if validPlace != []:
            while True:
                playerInput = input("")
                if playerInput in validInput:
                    inputChoice = strToInt(playerInput)
                    break
                else:
                    print(playerInput + ": Invalid choice")
                    print("Valid choices: ", end='')
                    # validChoice(validPlace)
                    print('inputchoice', inputChoice)
            # y = int(inputChoice[0])
            # x = int(inputChoice[1])

            # random code
            if validPlace != []:
                [y, x] = random.choice(validPlace)

            mainBoard = makeMove(mainBoard, turn, y, x)
        else:
            pass

    pointW = getScoreBoard(mainBoard)[W]
    pointB = getScoreBoard(mainBoard)[B]
    print("End of the game. W: ", getScoreBoard(mainBoard)[W], ", B: ",
          getScoreBoard(mainBoard)[B])
    if pointB >= pointW:
        print("B wins.")
    else:
        print("W wins.")

if __name__ == "__main__":
    main()
