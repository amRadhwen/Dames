from numpy import zeros, flipud
import pygame
import math

WIDTH = 600
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
DIMENSIONS = (10, 10)
SURFACE = DIMENSIONS[0]*DIMENSIONS[1]
PIECESNUMBER = int((DIMENSIONS[0]-2)/2)
SQUAREWIDTH = int(WIDTH / DIMENSIONS[0])
SQUAREHEIGHT = int(HEIGHT / DIMENSIONS[1])
BLACKPIECE = pygame.image.load("b_piece.png")
WHITEPIECE = pygame.image.load("w_piece.png")
#colors
#         R   G   B
LIGHT = (254,206,158)
DARK  = (209,139, 70)
BLACK = (  0,  0,  0)
WHITE = (255,255,255)

def createBoard(dimensions):
    return flipud(zeros(dimensions))

def fillBoard(board):
    coords = createBoardCoords()
    c = 0
    for x in range(DIMENSIONS[0]):
        for y in range(DIMENSIONS[1]):
            if board[x][y] == 1:
                screen.blit(BLACKPIECE, [coords[c][0]+5, coords[c][1]+2])
            elif board[x][y] == 2:
                screen.blit(WHITEPIECE, [coords[c][0]+5, coords[c][1]+2])
            c += 1
    

def createBoardCoords():
    board_coords = []
    y = 0
    while y < HEIGHT:
        for x in range(0, HEIGHT, SQUAREWIDTH):
            board_coords.append([x, y])
        y += SQUAREWIDTH
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
    print("Player: {0}".format(player))
    print("choice: {0}".format(choice))
    if player == 2:
        if moves:
            if moves.__len__() == 1:
                if choice == moves[0]:
                    board[origin[0]][origin[1]]  = 0
                    board[choice[0]][choice[1]] = 2 #same as using moves in place of moves with double index
                    return True
                else:
                    return False
            else:
                if choice in moves:
                    board[origin[0]][origin[1]]  = 0
                    board[choice[0]][choice[1]] = 2
                    return True
        else:
            return False
    else:
        if player == 1:
            if moves:
                if moves.__len__() == 1:
                    if choice == moves[0]:
                        board[origin[0]][origin[1]]  = 0
                        board[choice[0]][choice[1]] = 1 #same as using choice in place of moves with single index
                        return True
                    else:
                        return False
                else:
                    if choice in moves:
                        board[origin[0]][origin[1]]  = 0
                        board[choice[0]][choice[1]] = 1
                        return True
            else:
                return False

    



def drawBoard(board):
    coords = createBoardCoords()
    color = (DARK, LIGHT)
    color_inv = False
    row_inv = 1
    c = 0

    while c < coords.__len__():
        if row_inv > DIMENSIONS[0]:
            color_inv = not color_inv
            row_inv = 1
        pygame.draw.rect(screen, color[int(color_inv)], [coords[c][0], coords[c][1], SQUAREWIDTH, SQUAREHEIGHT])
        color_inv = not color_inv
        c += 1
        row_inv += 1
    fillBoard(board)

def toggleTurn(origin):
    x = origin[0]
    y = origin[1]
    return board[x][y]
            
        



pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Damme V1.0")
pygame.display.set_icon(pygame.image.load("dames.ico"))

#loop controller
gameEnd = False

#clock
clock = pygame.time.Clock()

#change the screen color to LIGHT
screen.fill(LIGHT)

board = createBoard(DIMENSIONS)
initBoard(board)
drawBoard(board)
#fillBoard(board)


#update the display
pygame.display.update()



print(board)
possibleMoves = False
origin = []
player = (1, 2)
player_inv = True
#Game main loop
while not gameEnd:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            gameEnd = True

        if e.type == pygame.MOUSEBUTTONDOWN:
            if not possibleMoves:
                posx = e.pos[0]
                posy = e.pos[1]
                x = int(math.floor(posx/SQUAREWIDTH))
                y = int(math.floor(posy/SQUAREHEIGHT))
                possibleMoves = checkMove(board, [y, x])
                origin = [y, x] #reversed because of matrix behaviour
                print("origin: "+str(origin))
                print("possibleMoves: "+str(possibleMoves))
                print(toggleTurn(origin))
            else:
                posx = e.pos[0]
                posy = e.pos[1]
                x = int(math.floor(posx/SQUAREWIDTH))
                y = int(math.floor(posy/SQUAREHEIGHT))
                choice = [y, x]
                eat(board, int(board[origin[0]][origin[1]]), origin, possibleMoves, choice)
                print(board)
                drawBoard(board)
                #fillBoard(board)
                pygame.display.update()
                origin = []
                possibleMoves = False

            



pygame.quit()