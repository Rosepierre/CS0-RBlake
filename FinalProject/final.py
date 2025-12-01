#Roger Blake
#2048 Final

import pygame
import random
import math

pygame.init()

#Constants:

FPS = 60

width, height = 800, 800
rows = 4 
colums = 4

rect_height = height // rows
rect_width = width // colums

outline_color = (202, 204, 206)
outline_thickness = 10 
background_color = (200, 190, 190)
font_color = (119, 110, 101)

font = pygame.font.SysFont("timesnewroman", 60, bold=True)
movement = 20

#pygame window start and window title
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("2048")


class Tile:
    COLORS = [
        (237, 229, 218),
        (238, 225, 201),
        (243, 178, 122),
        (246, 150, 101),
        (247, 124, 95),
        (247, 95, 59),
        (237, 208, 115),
        (237, 204, 99),
        (236, 202, 80),
        (237, 197, 63),
        (237, 194, 46),
    ]

    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.x = col * rect_width
        self.y = row * rect_height

    def get_color(self):
        color_index = int(math.log2(self.value)) - 1
        color = self.COLORS[color_index]
        return color
        

    def draw(self, window):
        color = self.get_color()
        pygame.draw.rect(window, color, (self.x, self.y, rect_width, rect_height))

        text = font.render(str(self.value), 1, font_color)
        window.blit(
            text,
            (
            self.x + (rect_width / 2 - text.get_width() / 2),
            self.y + (rect_height / 2 - text.get_height() / 2),
            )
        ) 

    def set_pos(self, ceil=False):
        if ceil:
            self.row = math.ceil(self.y / rect_height)
            self.col = math.ceil(self.x / rect_width)
        else:
            self.row = math.floor(self.y / rect_height)
            self.col = math.floor(self.x / rect_width)

    def move(self, delta):
        self.x += delta[0]
        self.y += delta[1]


def grid_drawing(window):
    for row in range(1, rows):
        y = row * rect_height
        pygame.draw.line(window, outline_color, (0, y), (width, y), outline_thickness)
    
    for colum in range(1, colums):
        x = colum * rect_width
        pygame.draw.line(window, outline_color, (x, 0), (x, height), outline_thickness)

    pygame.draw.rect(window, outline_color, (0, 0, width, height), outline_thickness)


def drawing(window, tiles):
    window.fill(background_color)

    for tile in tiles.values():
        tile.draw(window)

    grid_drawing(window)
    #updates in order of written
    pygame.display.update()


def get_random_pos(tiles):
    row = None
    col = None
    while True:
        row = random.randrange(0, rows)
        col = random.randrange(0, colums)

        if f"{row}{col}" not in tiles:
            break
    return row, col


def move_tiles(window, tiles, clock, direction):
    updated = True
    blocks = set()
    
    if direction == "left":
        sort_func = lambda x: x.col
        reverse = False
        delta = (-movement, 0)
        boundary_check = lambda tile: tile.col == 0
        get_next_tile = lambda tile: tiles.get(f"{tile.row}{tile.col - 1}")
        merge_check = lambda tile, next_tile: tile.x > next_tile.x + movement
        move_check = lambda tile, next_tile: tile.x > next_tile.x + rect_width
        ceil = True

    elif direction == "right":
        sort_func = lambda x: x.col
        reverse = True
        delta = (movement, 0)
        boundary_check = lambda tile: tile.col == colums - 1
        get_next_tile = lambda tile: tiles.get(f"{tile.row}{tile.col + 1}")
        merge_check = lambda tile, next_tile: tile.x < next_tile.x - movement
        move_check = lambda tile, next_tile: tile.x + rect_width+ movement < next_tile.x 
        ceil = False

    elif direction == "up":
        sort_func = lambda x: x.row
        reverse = False
        delta = (0, -movement)
        boundary_check = lambda tile: tile.row == 0
        get_next_tile = lambda tile: tiles.get(f"{tile.row - 1}{tile.col}")
        merge_check = lambda tile, next_tile: tile.y > next_tile.y + movement
        move_check = lambda tile, next_tile: tile.y > next_tile.y + rect_height
        ceil = True

    elif direction == "down":
        sort_func = lambda x: x.row
        reverse = True
        delta = (0, movement)
        boundary_check = lambda tile: tile.row == rows - 1
        get_next_tile = lambda tile: tiles.get(f"{tile.row + 1}{tile.col}")
        merge_check = lambda tile, next_tile: tile.y < next_tile.y - movement
        move_check = lambda tile, next_tile: tile.y + rect_height < next_tile.y 
        ceil = False

    while updated:
        clock.tick(FPS)
        updated = False
        sorted_tiles = sorted(tiles.values(), key=sort_func, reverse=reverse)

        for i, tile in enumerate(sorted_tiles):
            if boundary_check(tile):
                continue

            next_tile = get_next_tile(tile)
            if not next_tile:
                tile.move(delta)
            elif tile.value == next_tile.value and tile not in blocks and next_tile not in blocks:
                if merge_check(tile, next_tile):
                    tile.move(delta)
                else:
                    next_tile.value *= 2
                    sorted_tiles.pop(i)
                    blocks.add(next_tile)
            elif move_check(tile, next_tile):
                tile.move(delta)
            else:
                continue
            
            tile.set_pos(ceil)
            updated = True
        update_tiles(window, tiles, sorted_tiles)

    
    return end_move(tiles)

def end_move(tiles):
    for tile in tiles.values():
        if tile.value == 2048:
            return "winner"
    
    #Check for a loss
    if len(tiles) < rows * colums:
        pass
    else:
        
        for row in range(rows):
            for col in range(colums):
                current = tiles.get(f"{row}{col}")
                
                right = tiles.get(f"{row}{col+1}")
                if right and right.value == current.value:
                    return "continue"
                
                down = tiles.get(f"{row+1}{col}")
                if down and down.value == current.value:
                    return "continue"
        
        return "lost"

    row, col = get_random_pos(tiles)
    tiles[f"{row}{col}"] = Tile(random.choice([2, 4]), row, col)
    return "continue"

def update_tiles(window, tiles, sorted_tiles):
    tiles.clear()
    for tile in sorted_tiles:
        tiles[f"{tile.row}{tile.col}"] = tile
    drawing(window, tiles)


def generate_tiles():
    tiles = {}
    for _ in range(2):
        row, col = get_random_pos(tiles)
        tiles[f"{row}{col}"] = Tile(random.choice([2, 4]), row, col)
    return tiles


def main(window):
    clock = pygame.time.Clock()
    run = True
    tiles = generate_tiles()

    game_state = "continue"

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN and game_state == "continue":

                if event.key == pygame.K_LEFT:
                    game_state = move_tiles(window, tiles, clock, "left")

                elif event.key == pygame.K_RIGHT:
                    game_state = move_tiles(window, tiles, clock, "right")

                elif event.key == pygame.K_UP:
                    game_state = move_tiles(window, tiles, clock, "up")

                elif event.key == pygame.K_DOWN:
                    game_state = move_tiles(window, tiles, clock, "down")

        drawing(window, tiles)

        if game_state in ["winner", "lost"]:
            window.fill(background_color)
            text = font.render(
                "You Win!" if game_state == "winner" else "Game Over!", True, font_color
            )
            window.blit(
                text,
                (
                    width // 2 - text.get_width() // 2,
                    height // 2 - text.get_height() // 2,
                ),
            )
            pygame.display.update()
            pygame.time.delay(5000) 
            run = False
        

if __name__ == "__main__":
    main(window)