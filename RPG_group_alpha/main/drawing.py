from RPG_group_alpha import parent_file as p_f
from RPG_group_alpha.world.world import draw_map
from RPG_group_alpha.player.player import player
from RPG_group_alpha.textures import division_and_organisation as dao


def draw_screen():
    p_f.screen.fill((120, 160, 250, 250))

    draw_map()
    for thing in p_f.todraw['things']:
        p_f.pygame.draw.rect(p_f.screen, thing['color'], thing['body'])
        if thing['text'] is not None:
            p_f.screen.blit(p_f.objectsfont.render(thing['text'], 1, (255, 255, 255, 255)),
                            (thing['body'].x + 1, thing['body'].y + 1))

    for creature in p_f.creaturesmap[p_f.actualmap]:
        p_f.pygame.draw.rect(p_f.screen, creature.color, creature.body)

    for icon in p_f.todraw['icons'].values():
        if type(icon) == dict:
            p_f.pygame.draw.rect(p_f.screen, icon['color'], icon['body'])
        else:
            p_f.screen.blit(icon[0], icon[1])
            if len(icon) > 2:
                if icon[2] > 0:
                    icon[2] -= 1
                else:
                    p_f.todraw["icons"].__delitem__(list(p_f.todraw["icons"].keys())[list(p_f.todraw["icons"].values()).
                                                    index(icon)])
                    break

    def player_animation(type):
        p_f.screen.blit(dao.playeranimation[type][player.actualanimationflip], (player.body.x-20, player.body.y))
        p_f.screen.blit(dao.knifeanimation[type][player.actualanimationflip], (player.body.x-20, player.body.y))

    player_animation(player.animation)


def update_animations_flips():
    while p_f.running:
        player.actualanimationflip = (player.actualanimationflip + 1) % dao.playeranimation[player.animation].__len__()
        p_f.pygame.time.delay(dao.delays['playeranimation ' + player.animation])

        if player.animation == 'attack':
            if player.actualanimationflip == dao.playeranimation[player.animation].__len__() - 1:
                player.animation = 'breathing'
                player.actualanimationflip = 0

        p_f.clock.tick(p_f.tick)
        p_f.threadCenter.sleep()


p_f.threadCenter.append(update_animations_flips)
