from RPG_group_alpha import parent_file as p_f
from RPG_group_alpha.creatures.species import Robber


creaturesmap = {1: [],
                2: [Robber((870, 260), 1)]}


def update_actual_map_creatures():
    global creaturesmap

    while p_f.running:
        for creature in creaturesmap[p_f.actualmap]:
            creature.update()

            p_f.clock.tick(p_f.tick)


p_f.threadCenter.append(update_actual_map_creatures)
