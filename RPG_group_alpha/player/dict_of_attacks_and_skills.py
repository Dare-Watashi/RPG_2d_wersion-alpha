from RPG_group_alpha import parent_file as p_f


maindict = {
    'fraction': {'normal attack': {'damage': 'multiplier', 'animation': 'animation type'},
                 'skill 1': {'damage': 'multiplier', 'animation': 'animation type', 'cooldown': 'time in seconds',
                             'energy regeneration': 'energy amount'},
                 'skill 2': {'damage': 'multiplier', 'animation': 'animation type', 'cooldown': 'time in seconds',
                             'energy regeneration': 'energy amount'},
                 'skill 3': {'damage': 'multiplier', 'animation': 'animation type', 'cooldown': 'time in seconds',
                             'energy regeneration': 'energy amount'},
                 'burst': {'damage': 'multiplier', 'animation': 'animation type', 'cooldown': 'time in seconds',
                           'cost': 'energy amount'}},

    'basic': {'normal attack': {'damage': '1', 'animation': 'knife'},
              'skill 1': {'damage': '1.1', 'animation': 'animation type', 'cooldown': 5, 'energy regeneration': 5},
              'skill 2': {'damage': '1.15', 'animation': 'animation type', 'cooldown': 5, 'energy regeneration': 5},
              'skill 3': {'damage': '1.2', 'animation': 'animation type', 'cooldown': 5, 'energy regeneration': 5},
              'burst': {'damage': '1.5', 'animation': 'animation type', 'cooldown': 15, 'cost': 50}},

}


def execute(executor, activation, skilltype, skilllevel):
    def rush(executor, faceing, distance, active):
        active = True
        executor.animation = 'skill1active'
        executor.actualanimationflip = 0

        for i in range(int(distance / 100 * p_f.tick)):
            executor.body.x += faceing[0] * 100 / p_f.tick
            executor.body.y += faceing[1] * 100 / p_f.tick
            p_f.clock.tick(p_f.tick*4)

        active = False
        executor.animation = 'breathing'

    if skilltype == 'rush':
        p_f.threadCenter.append(target=rush, args=(executor, executor.faceing, 50+50*skilllevel, activation))
