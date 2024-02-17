import pygame
import sys
import time
from copy import deepcopy

def draw_grid(matrix):
    global sound

    return_surf = pygame.image.load('return.png')
    return_rect = return_surf.get_rect(topleft=(600, 0))
    screen.blit(return_surf, return_rect)

        
    if sound == True:
        return_surf_2 = pygame.image.load('sound.png')
        return_rect_2 = return_surf.get_rect(topleft=(500, 0))
        screen.blit(return_surf_2, return_rect_2)
    else:
        return_surf_2 = pygame.image.load('no_sound.png')
        return_rect_2 = return_surf_2.get_rect(topleft=(500, 0))
        screen.blit(return_surf_2, return_rect_2)
    pygame.display.update()

    rect = pygame.Rect(710, 10, 35, 35)
    pygame.draw.rect(screen, white, rect, 0)
    rect = pygame.Rect(755, 10, 35, 35)
    pygame.draw.rect(screen, white, rect, 0)
    rect = pygame.Rect(755, 55, 35, 35)
    pygame.draw.rect(screen, white, rect, 0)
    rect = pygame.Rect(710, 55, 35, 35)
    pygame.draw.rect(screen, white, rect, 0)


    maxx = (max(len(matrix), len(matrix[0])))
    blockSize = (window_height - 200)//maxx
    if len(matrix) == len(matrix[0]) < 6:
        for x in range(100, len(matrix[0])*blockSize, blockSize):
            for y in range(100, len(matrix)*blockSize, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                if matrix[(y-100)//((window_height-200)//maxx)][(x-100)//((window_height-200)//maxx)] == "#":
                    pygame.draw.rect(screen, gray, rect, 0)
                elif matrix[(y-100)//((window_height-200)//maxx)][(x-100)//((window_height-200)//maxx)] == "W":
                    pygame.draw.rect(screen, white, rect, 0)
                elif matrix[(y-100)//((window_height-200)//maxx)][(x-100)//((window_height-200)//maxx)] == "R":
                    pygame.draw.rect(screen, red, rect, 0)
                elif matrix[(y-100)//((window_height-200)//maxx)][(x-100)//((window_height-200)//maxx)] == "Y":
                    pygame.draw.rect(screen, yellow, rect, 0)
                elif matrix[(y-100)//((window_height-200)//maxx)][(x-100)//((window_height-200)//maxx)] == "B":
                    pygame.draw.rect(screen, blue, rect, 0)
                elif matrix[(y-100)//((window_height-200)//maxx)][(x-100)//((window_height-200)//maxx)] == "G":
                    pygame.draw.rect(screen, green, rect, 0)
                elif matrix[(y-100)//((window_height-200)//maxx)][(x-100)//((window_height-200)//maxx)] == "V":
                    pygame.draw.rect(screen, violet, rect, 0)
                else:
                    pygame.draw.rect(screen, black, rect, 0)
    else:
        for x in range(100, (len(matrix[0])+1)*blockSize, blockSize):
            for y in range(100, (len(matrix)+1)*blockSize, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                if matrix[(y-100)//((window_height-200)//maxx)][(x-100)//((window_height-200)//maxx)] == "#":
                    pygame.draw.rect(screen, gray, rect, 0)
                elif matrix[(y-100)//((window_height-200)//maxx)][(x-100)//((window_height-200)//maxx)] == "W":
                    pygame.draw.rect(screen, white, rect, 0)
                elif matrix[(y-100)//((window_height-200)//maxx)][(x-100)//((window_height-200)//maxx)] == "R":
                    pygame.draw.rect(screen, red, rect, 0)
                elif matrix[(y-100)//((window_height-200)//maxx)][(x-100)//((window_height-200)//maxx)] == "Y":
                    pygame.draw.rect(screen, yellow, rect, 0)
                elif matrix[(y-100)//((window_height-200)//maxx)][(x-100)//((window_height-200)//maxx)] == "B":
                    pygame.draw.rect(screen, blue, rect, 0)
                elif matrix[(y-100)//((window_height-200)//maxx)][(x-100)//((window_height-200)//maxx)] == "G":
                    pygame.draw.rect(screen, green, rect, 0)
                elif matrix[(y-100)//((window_height-200)//maxx)][(x-100)//((window_height-200)//maxx)] == "V":
                    pygame.draw.rect(screen, violet, rect, 0)
                else:
                    pygame.draw.rect(screen, black, rect, 0)
    


def levels_list(levels):
    global coords_list
    coords_list = []
    screen.fill(black)

    return_surf = pygame.image.load('return.png')
    return_rect = return_surf.get_rect(topleft=(690, 0))
    screen.blit(return_surf, return_rect)

    counter = 0
    row = 1
    for _ in range(len(levels)):
        counter += 1
        rect = pygame.Rect(counter*100, row*100, 80, 80)
        coords_list.append([counter*100, row*100, counter*100+80, row*100+80])
        if is_symmetric(levels[_]):
            pygame.draw.rect(screen, green, rect, 0)
        else:
            pygame.draw.rect(screen, red, rect, 0)
        if counter == 6:
            counter = 0
            row += 1




def is_symmetric(matrix):
    matrix_2 = []
    for _ in matrix:
        matrix_2.append(_[::-1])
    if matrix == matrix_2:
        return True
    else:
        return False
    

def W_coords(matrix):
    coords = []
    for _ in matrix:
        if "W" in _:
            coords.append(matrix.index(_))
            coords.append(_.index("W"))
            return coords
        

def write_matrices(matrix, matrix_name, filename):
    with open(filename, 'a') as f:
        f.write(f'{matrix_name} = [' + ', '.join([str(x) for x in matrix]) + ']\n')
        

def osnova(levels_local):
    global levels_frozen, sound, moves, levels
    for matrix in levels_local:
        screen.fill(black)
        while not is_symmetric(matrix):
            draw_grid(matrix)
            w = W_coords(matrix)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    f = open('matrix_file.txt', 'r+')
                    f.truncate(0)
                    for _ in range(len(levels)):
                        write_matrices(levels[_], f'level_{_+1}', 'matrix_file.txt')
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    _ = [700, 0, 800, 100]
                    if _[0] <= pos[0] and pos[0] <= _[2] and _[1] <= pos[1] and pos[1] <= _[3]:
                        levels_menu(levels_frozen)
                    _ = [600, 0, 700, 100]
                    if _[0] <= pos[0] and pos[0] <= _[2] and _[1] <= pos[1] and pos[1] <= _[3]:
                        return matrix
                    _ = [500, 0, 700, 100]
                    if _[0] <= pos[0] and pos[0] <= _[2] and _[1] <= pos[1] and pos[1] <= _[3]:
                        if sound == True:
                            sound = False
                            pygame.mixer.Channel(0).pause()
                        else:
                            sound = True
                            pygame.mixer.Channel(0).unpause()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                            if matrix[w[0]][w[1]-1] == "0":
                                matrix[w[0]][w[1]] = "0"
                                matrix[w[0]][w[1]-1] = "W"
                                moves += 1
                                pygame.mixer.music.load("move.mp3")
                                pygame.mixer.music.play(1)
                            elif matrix[w[0]][w[1]-1] != "#":
                                if matrix[w[0]][w[1]-2] == "0":
                                    matrix[w[0]][w[1]-2] = matrix[w[0]][w[1]-1]
                                    matrix[w[0]][w[1]] = "0"
                                    matrix[w[0]][w[1]-1] = "W"
                                    moves += 1
                                    pygame.mixer.music.load("move.mp3")
                                    pygame.mixer.music.play(1)
                    elif event.key == pygame.K_RIGHT:
                            if matrix[w[0]][w[1]+1] == "0":
                                matrix[w[0]][w[1]] = "0"
                                matrix[w[0]][w[1]+1] = "W"
                                moves += 1
                                pygame.mixer.music.load("move.mp3")
                                pygame.mixer.music.play(1)
                            elif matrix[w[0]][w[1]+1] != "#":
                                if matrix[w[0]][w[1]+2] == "0":
                                    matrix[w[0]][w[1]+2] = matrix[w[0]][w[1]+1]
                                    matrix[w[0]][w[1]] = "0"
                                    matrix[w[0]][w[1]+1] = "W"
                                    moves += 1
                                    pygame.mixer.music.load("move.mp3")
                                    pygame.mixer.music.play(1)
                    elif event.key == pygame.K_UP:
                            if matrix[w[0]-1][w[1]] == "0":
                                matrix[w[0]][w[1]] = "0"
                                matrix[w[0]-1][w[1]] = "W"
                                moves += 1
                                pygame.mixer.music.load("move.mp3")
                                pygame.mixer.music.play(1)
                            elif matrix[w[0]-1][w[1]] != "#":
                                if matrix[w[0]-2][w[1]] == "0":
                                    matrix[w[0]-2][w[1]] = matrix[w[0]-1][w[1]]
                                    matrix[w[0]][w[1]] = "0"
                                    matrix[w[0]-1][w[1]] = "W"
                                    moves += 1
                                    pygame.mixer.music.load("move.mp3")
                                    pygame.mixer.music.play(1)
                    elif event.key == pygame.K_DOWN:
                            if matrix[w[0]+1][w[1]] == "0":
                                matrix[w[0]][w[1]] = "0"
                                matrix[w[0]+1][w[1]] = "W"
                                moves += 1
                                pygame.mixer.music.load("move.mp3")
                                pygame.mixer.music.play(1)
                            elif matrix[w[0]+1][w[1]] != "#":
                                if matrix[w[0]+2][w[1]] == "0":
                                    matrix[w[0]+2][w[1]] = matrix[w[0]+1][w[1]]
                                    matrix[w[0]][w[1]] = "0"
                                    matrix[w[0]+1][w[1]] = "W"
                                    moves += 1
                                    pygame.mixer.music.load("move.mp3")
                                    pygame.mixer.music.play(1)
                    if is_symmetric(matrix):
                        draw_grid(matrix)
            pygame.display.update()
        time.sleep(1)
        return matrix
    

def levels_menu(levels_loc):
    global levels
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    f = open('matrix_file.txt', 'r+')
                    f.truncate(0)
                    for _ in range(len(levels)):
                        write_matrices(levels[_], f'level_{_+1}', 'matrix_file.txt')
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    _ = [690, 0, 790, 100]
                    if _[0] <= pos[0] and pos[0] <= _[2] and _[1] <= pos[1] and pos[1] <= _[3]:
                        loaded_matrices = {}
                        with open('matrix_file_freeze.txt', 'r') as file:
                            exec(file.read(), loaded_matrices)
                        loaded_matrices.pop(next(iter(loaded_matrices)))
                        levels = list(loaded_matrices.values())
                        start(levels)

                    else:
                        for _ in coords_list:
                            if _[0] <= pos[0] and pos[0] <= _[2] and _[1] <= pos[1] and pos[1] <= _[3]:
                                while True:
                                    a = osnova(deepcopy([levels_loc[coords_list.index(_)]]))
                                    if is_symmetric(a):
                                        levels[coords_list.index(_)] = a
                                        break
        levels_list(levels)
        counter = 0
        for _ in levels:
            if is_symmetric(_):
                counter += 1
        if counter == len(levels):
            finish()
        pygame.display.update()


def draw_line_round_corners_polygon(surf, p1, p2, c, w):
    p1v = pygame.math.Vector2(p1)
    p2v = pygame.math.Vector2(p2)
    lv = (p2v - p1v).normalize()
    lnv = pygame.math.Vector2(-lv.y, lv.x) * w // 2
    pts = [p1v + lnv, p2v + lnv, p2v - lnv, p1v - lnv]
    pygame.draw.polygon(surf, c, pts)
    pygame.draw.circle(surf, c, p1, round(w / 2))
    pygame.draw.circle(surf, c, p2, round(w / 2))

def start(levels):
    screen.fill(black)
    f1 = pygame.font.Font(None, 100)
    text = f1.render('Symmetry', True, white)
    screen.blit(text, (225, 100))
    draw_line_round_corners_polygon(screen, (350, 300), (350, 450), "white", 20)
    draw_line_round_corners_polygon(screen, (350, 300), (450, 375), "white", 20)
    draw_line_round_corners_polygon(screen, (350, 450), (450, 375), "white", 20)
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    f = open('matrix_file.txt', 'r+')
                    f.truncate(0)
                    for _ in range(len(levels)):
                        write_matrices(levels[_], f'level_{_+1}', 'matrix_file.txt')
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    _ = (340, 290, 460, 460)
                    if _[0] <= pos[0] and pos[0] <= _[2] and _[1] <= pos[1] and pos[1] <= _[3]:
                        levels_menu(levels)

        pygame.display.update()
    
def finish():
    global moves
    screen.fill(black)
    f1 = pygame.font.Font(None, 100)
    text = f1.render('You won!', True, white)
    screen.blit(text, (225, 350))
    text = f1.render(f'moves: {moves}', True, white)
    screen.blit(text, (225, 500))
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        pygame.display.update()



black = (0, 0, 0)
white = (200, 200, 200)
gray = (42, 42, 42)
red = (255, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
green = (0, 128, 0)
violet = (139, 0, 255)


window_height = 800
window_width = 800

loaded_matrices = {}
with open('matrix_file.txt', 'r') as file:
    exec(file.read(), loaded_matrices)


loaded_matrices.pop(next(iter(loaded_matrices)))

levels = list(loaded_matrices.values())
levels_frozen = deepcopy(levels)

pygame.init()
pygame.mixer.Channel(0).play(pygame.mixer.Sound('Sponge Bob Square Pants Theme.mp3'))
sound = True

moves = 0



def main():
    global screen, clock
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Symmetry')
    a = pygame.image.load('icon.png')
    pygame.display.set_icon(a)

    start(levels)
    

         

if __name__ == '__main__':
    main()