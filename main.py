from numpy import zeros, flipud
import pygame

WIDTH = 600
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
DIMENSIONS = (10, 10)
SURFACE = DIMENSIONS[0]*DIMENSIONS[1]
PIECESNUMBER = int((DIMENSIONS[0]-2)/2)

#colors
LIGHT = (254,206,158)
DARK = (209,139,70)

def createBoard(dimensions):
    return flipud(zeros(dimensions))

def fillBoard():
    pass

def createBoardCoords():
    board_coords = []
    y = 0
    while y < HEIGHT:
        for x in range(0, HEIGHT, 75):
            board_coords.append([x, y])
        y += 75
    return board_coords

def initBoard(board):
    mod = (0, 1)
    inv = True
    for x in range(PIECESNUMBER):
        inv = int(not inv)
        for y in range(DIMENSIONS[1]):
            if y % 2 != inv:
                board[x][y] = 2
    
    for x in range(DIMENSIONS[0]-1, PIECESNUMBER+1, -1):
        inv = int(not inv)
        for y in range(DIMENSIONS[1]):
            if y % 2 == inv:
                board[x][y] = 1

def checkMove(board, coords):
    current = board[coords[0]][coords[1]]
    if current == 1 or current == 2:
        if current == 2:
            x = coords[0]+1
            ly = coords[1]-1
            ry = coords[1]+1
            if x in range(10):
                if ly in range(10) and ry in range(10):
                    return [[x, ly], [x, ry]]
                elif ly in range(10) and ry not in range(10):
                    return [[x, ly]]
                elif ly not in range(10) and ry in range(10):
                    return [[x, ry]]
                else:
                    return False
            else:
                return False
        else:
            x = coords[0]-1
            ly = coords[1]-1
            ry = coords[1]+1
            if x in range(10):
                if ly in range(10) and ry in range(10):
                    return [[x, ly], [x, ry]]
                elif ly in range(10) and ry not in range(10):
                    return [[x, ly]]
                elif ly not in range(10) and ry in range(10):
                    return [[x, ry]]
                else:
                    return False
            else:
                return False

    else:
        return False

def eat(board, player, origin, moves, choice):
    if player == 2:
        if moves:
            if moves.__len__() == 1:
                if choice == moves[0]:
                    board[origin[0]][origin[1]]  = 0
                    board[moves[0][0]][moves[0][1]] = 2 #same as using choice in place of moves
                    return True
                else:
                    return False
            else:
                if choice in moves:
                    board[origin[0]][origin[1]]  = 0
                    board[choice[0][0]][choice[0][1]] = 2
                    return True
        else:
            return False
    else:
        if player == 1:
        if moves:
            if moves.__len__() == 1:
                if choice == moves[0]:
                    board[origin[0]][origin[1]]  = 0
                    board[moves[0][0]][moves[0][1]] = 1 #same as using choice in place of moves
                    return True
                else:
                    return False
            else:
                if choice in moves:
                    board[origin[0]][origin[1]]  = 0
                    board[choice[0][0]][choice[0][1]] = 1
                    return True
        else:
            return False
    



def drawBoard():
    coords = createBoardCoords()
    color = (DARK, LIGHT)
    color_inv = False
    row_inv = 1
    c = 0

    while c < coords.__len__():
        if row_inv > 8:
            color_inv = not color_inv
            row_inv = 1
        pygame.draw.rect(screen, color[int(color_inv)], [coords[c][0], coords[c][1], 75, 75])
        color_inv = not color_inv
        c += 1
        row_inv += 1

board = createBoard(DIMENSIONS)

initBoard(board)
print(board)
print(checkMove(board, [6, 1]).__len__())
print(checkMove(board, [0, 9]).__len__())


#pygame.init()
#screen = pygame.display.set_mode(SIZE)
#pygame.display.set_caption("Damme V1.0")
#
##loop controller
#gameEnd = False
#
##clock
#clock = pygame.time.Clock()
#
##change the screen color to LIGHT
#screen.fill(LIGHT)
#drawBoard()
#print(createBoard(DIMENSIONS))
#
#
##update the display
#pygame.display.update()
#
##Game main loop
#while not gameEnd:
#    for e in pygame.event.get():
#        if e.type == pygame.QUIT:
#            gameEnd = True
#
#
#pygame.quit()