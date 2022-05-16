import parent_file as p_f
from block import Block
from player import player


screen_width, screen_height = p_f.screen_width//50 + 1, p_f.screen_height//50 + 1
width, height = 24, 18
world = []


'''def fillmap():
    for y in range(height):
        for x in range(width):
            if y > 12:
                world[x][y].append(Block((x*50, y*50), (50, 50), 'dirt', 'dirt', ['dirt']))
            else:
                world[x][y].append(Block((x*50, y*50), (50, 50), 'sky', 'sky'))'''


def drawworld():
    for y in range(height):
        for x in range(width):
            p_f.pygame.draw.rect(p_f.screen, world[x][y].color, world[x][y].body)
