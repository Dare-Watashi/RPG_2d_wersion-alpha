from RPG_group_alpha import parent_file as p_f
from RPG_group_alpha.world.world import draw_map
from RPG_group_alpha.player.player import player


todraw = []


def draw_screen():
    p_f.screen.fill((120, 160, 250, 250))

    draw_map()
    for thing in todraw:
        p_f.pygame.draw.rect(p_f.screen, thing['color'], thing['body'])
        if thing['text'] is not None:
            p_f.screen.blit(p_f.objectsfont.render(thing['text'], 1, (255, 255, 255, 255)),
                            (thing['body'].x + 1, thing['body'].y + 1))
    p_f.pygame.draw.rect(p_f.screen, player.normalcolor, player.body)
