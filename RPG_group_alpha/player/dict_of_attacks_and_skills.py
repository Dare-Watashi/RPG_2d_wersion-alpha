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


def hurt_targets_in_range(executor, damage, exceptors=[]):
    targets = []

    for creature in p_f.creaturesmap[p_f.actualmap]:
        if creature.body.colliderect(executor.normalattackcollisioner):
            if creature not in exceptors:
                targets.append(creature)
                exceptors.append(creature)

    for target in targets:
        target.life -= damage

    return exceptors


def execute(executor, activation, skilltype, skilllevel, skillnumber):
    def rush(executor, faceing, distance, active, skillnumber):
        global maindict

        active = True
        executor.animation = 'skill1active'
        executor.actualanimationflip = 0

        damage = executor.damage * float(maindict[executor.fraction][skillnumber]['damage'])

        exceptors = []

        for i in range(int(distance / 100 * p_f.tick)):
            executor.body.x += faceing[0] * 100 / p_f.tick
            executor.body.y += faceing[1] * 100 / p_f.tick
            p_f.clock.tick(p_f.tick*4)
            exceptors = hurt_targets_in_range(executor=executor, damage=damage, exceptors=exceptors)

        active = False
        executor.animation = 'breathing'

    if skilltype == 'rush':
        p_f.threadCenter.append(target=rush, args=(executor, executor.faceing, 50+50*skilllevel, activation,
                                                   skillnumber))
