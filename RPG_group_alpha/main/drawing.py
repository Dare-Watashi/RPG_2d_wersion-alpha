from RPG_group_alpha import parent_file as p_f
from RPG_group_alpha.world.world import draw_map
from RPG_group_alpha.player.player import player
from RPG_group_alpha.textures import division_and_organisation as dao


todraw = []

actualplayeranimationflip = 0


def draw_screen():
    p_f.screen.fill((120, 160, 250, 250))

    draw_map()
    for thing in todraw:
        p_f.pygame.draw.rect(p_f.screen, thing['color'], thing['body'])
        if thing['text'] is not None:
            p_f.screen.blit(p_f.objectsfont.render(thing['text'], 1, (255, 255, 255, 255)),
                            (thing['body'].x + 1, thing['body'].y + 1))

    def player_animation(type):
        global actualplayeranimationflip

        p_f.screen.blit(dao.playeranimation[type][actualplayeranimationflip], (player.body.x-20, player.body.y))

    player_animation('breathing')


def update_animations_flips():
    global actualplayeranimationflip
    while p_f.running:
        actualplayeranimationflip = (actualplayeranimationflip + 1) % dao.playeranimation['breathing'].__len__()
        p_f.pygame.time.delay(dao.delays['playeranimation breathing'])
        p_f.clock.tick(p_f.tick)


p_f.threadCenter.append(update_animations_flips)
