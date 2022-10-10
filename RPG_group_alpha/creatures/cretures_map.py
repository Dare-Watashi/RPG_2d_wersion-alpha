from RPG_group_alpha import parent_file as p_f
from RPG_group_alpha.creatures.species import Robber


def update_actual_map_creatures():
    p_f.creaturesmap = {1: [],
                        2: [Robber((870, 260), 1)]}
    while p_f.running:
        for creature in p_f.creaturesmap[p_f.actualmap]:
            if not p_f.playersmenuopened:
                creature.update()

        p_f.clock.tick(p_f.tick)
        p_f.threadCenter.sleep()


def activate_update_actual_map_creatures():
    global update_actual_map_creatures
    p_f.threadCenter.append(update_actual_map_creatures)
