from RPG_group_alpha import parent_file as p_f
from RPG_group_alpha.world.world_maps import maps
from RPG_group_alpha.player.elements_classes import elements
from RPG_group_alpha.player import dict_of_attacks_and_skills as dict_of_skills
from RPG_group_alpha.creatures.cretures_map import creaturesmap


class Player:
    def __init__(self, place, size, element,
                 maxlife, maxhealth, maxdefense, maxdamage, maxattackspeed, maxcriticalchance, maxcriticalmultiplier,
                 maxspeed, fraction):
        """ ********** general **********"""
        self.progress, self.maxprogress = 0, 100
        self.level = 1
        self.rank = 1

        self.element = elements[element]
        self.fraction = fraction

        """ ********** characteristic ********** """
        self.levelinglife = maxlife
        self.maxlife = maxlife
        self.life = self.maxlife * self.element.multipliers['life']
        self.levelinghealth = maxhealth
        self.maxhealth = maxhealth
        self.health = self.maxhealth * self.element.multipliers['health']
        self.levelingdefense = maxdefense
        self.maxdefense = maxdefense
        self.defense = self.maxdefense * self.element.multipliers['defense']

        self.levelingdamage = maxdamage
        self.maxdamage = maxdamage
        self.damage = self.maxdamage * self.element.multipliers['damage']
        self.maxattackspeed = maxattackspeed  # 2 hits per second
        self.attackspeed = self.maxattackspeed * self.element.multipliers['attack speed']
        self.levelingcriticalchance = maxcriticalchance
        self.maxcriticalchance = maxcriticalchance
        self.criticalchance = self.maxcriticalchance * self.element.multipliers['critical chance']
        self.levelingcriticalmultiplier = maxcriticalmultiplier
        self.maxcriticalmultiplier = maxcriticalmultiplier
        self.criticalmultiplier = self.maxcriticalmultiplier * self.element.multipliers['critical multiplier']

        self.maxspeed = maxspeed
        self.runspeed = 5 / 4 * self.maxspeed
        self.walkspeed = 3 / 4 * self.maxspeed
        self.speed = self.walkspeed * self.element.multipliers['movement speed']

        """ ********** body ********* """
        self.normalscale = size
        self.scale = self.normalscale

        self.body = p_f.pygame.Rect(place, self.scale)
        self.normalcolor = p_f.pygame.Color(200, 150, 160, 255)
        self.color = self.normalcolor

        self.faceing = [1, 0]

        """ ********** animation ********* """
        self.animation = 'breathing'
        self.actualanimationflip = 0

        """ ********** fight ********* """
        self.moveing = False
        self.attacking = False
        self.normalattackcooldown = p_f.tick * 2

        self.skill1 = 'rush'
        self.skill1cooldown = 0
        self.skill1level = 1
        self.skill1active = False
        p_f.todraw['icons']['skill1-background'] = {'body': p_f.pygame.Rect(p_f.mapcorners[p_f.actualmap][2] - 150,
                                                            p_f.mapcorners[p_f.actualmap][3] - 50, 50, 50),
                                                    'color': p_f.pygame.Color(15, 120, 52)}

        p_f.todraw['icons']['skill1-ability'] = {'body':
                                                 p_f.pygame.Rect(p_f.mapcorners[p_f.actualmap][2] - 150,
                                                                 p_f.mapcorners[p_f.actualmap][3] - 50, 50,
                                                                 50 - self.skill1cooldown),
                                                 'color': p_f.pygame.Color(20, 180, 70)}

        p_f.todraw['icons']['skill1-ability-number'] = (p_f.skillsfont.render('1', 1, p_f.pygame.Color(33, 250, 180)),
                                                        (p_f.mapcorners[p_f.actualmap][2] - 136,
                                                         p_f.mapcorners[p_f.actualmap][3] - 48))

        self.skill2 = None
        self.skill3 = None
        self.burst = None

        """ ********** thread **********"""
        self.functionsthread = p_f.threadCenter.append(self.calling_functions, name='_player functions thread_')

    def calling_functions(self):
        while p_f.running:
            self.move()
            self.attack()
            self.level_up()

            p_f.clock.tick(p_f.tick)

    def update_characteristic(self):
        self.maxlife = int(self.level * self.levelinglife * (9 + self.rank) / 10)
        self.life = self.maxlife * self.element.multipliers['life']
        self.maxhealth = int(self.level * self.levelinghealth * (9 + self.rank) / 10)
        self.health = self.maxhealth * self.element.multipliers['health']
        self.maxdefense = int(self.level * self.levelingdefense * (9 + self.rank) / 10)
        self.life = self.maxlife * self.element.multipliers['defense']

        self.maxdamage = int(self.level * self.levelingdamage * (9 + self.rank) / 10)
        self.damage = self.maxdamage * self.element.multipliers['damage']
        self.maxcriticalchance = int(self.level * self.levelingcriticalchance * (9 + self.rank) / 10)
        self.criticalchance = self.maxcriticalchance * self.element.multipliers['critical chance']
        self.maxcriticalmultiplier = int(self.level * self.levelingcriticalmultiplier * (9 + self.rank) / 10)
        self.criticalmultiplier = self.maxcriticalmultiplier * self.element.multipliers['critical multiplier']

    def move(self):
        if not (self.attacking or self.skill1active):
            pos = self.body.x, self.body.y

            if p_f.pygame.key.get_pressed()[p_f.pygame.K_LSHIFT]:
                self.speed = p_f.mps(self.walkspeed) * self.element.multipliers['movement speed']

            if p_f.pygame.key.get_pressed()[p_f.pygame.K_LCTRL]:
                self.speed = p_f.mps(self.runspeed) * self.element.multipliers['movement speed']

            if p_f.pygame.key.get_pressed()[p_f.pygame.K_d]:
                if p_f.pygame.key.get_pressed()[p_f.pygame.K_w] or p_f.pygame.key.get_pressed()[p_f.pygame.K_s]:
                    self.body.x += (self.speed / p_f.clock.get_fps() + 0.01) * p_f.numpy.sin(45)
                    self.faceing[0] = 1 * p_f.numpy.sin(45)
                else:
                    self.body.x += self.speed / p_f.clock.get_fps() + 0.01
                    self.faceing = [1, 0]

            if p_f.pygame.key.get_pressed()[p_f.pygame.K_a]:
                if p_f.pygame.key.get_pressed()[p_f.pygame.K_w] or p_f.pygame.key.get_pressed()[p_f.pygame.K_s]:
                    self.body.x -= (self.speed / p_f.clock.get_fps() + 0.01) * p_f.numpy.sin(45)
                    self.faceing[0] = -1 * p_f.numpy.sin(45)
                else:
                    self.body.x -= self.speed / p_f.clock.get_fps() + 0.01
                    self.faceing = [-1, 0]

            if p_f.pygame.key.get_pressed()[p_f.pygame.K_w]:
                if p_f.pygame.key.get_pressed()[p_f.pygame.K_a] or p_f.pygame.key.get_pressed()[p_f.pygame.K_d]:
                    self.body.y -= (self.speed / p_f.clock.get_fps() + 0.01) * p_f.numpy.sin(45)
                    self.faceing[1] = -1 * p_f.numpy.sin(45)
                else:
                    self.body.y -= self.speed / p_f.clock.get_fps() + 0.01
                    self.faceing = [0, -1]

            if p_f.pygame.key.get_pressed()[p_f.pygame.K_s]:
                if p_f.pygame.key.get_pressed()[p_f.pygame.K_a] or p_f.pygame.key.get_pressed()[p_f.pygame.K_d]:
                    self.body.y += (self.speed / p_f.clock.get_fps() + 0.01) * p_f.numpy.sin(45)
                    self.faceing[1] = 1 * p_f.numpy.sin(45)
                else:
                    self.body.y += self.speed / p_f.clock.get_fps() + 0.01
                    self.faceing = [0, 1]

            p_f.pygame.time.delay(20)

            if pos == (self.body.x, self.body.y):
                self.moveing = False
            else:
                self.moveing = True

            if maps[p_f.actualmap]['walkable'].body.right < self.body.right:
                self.body.right = maps[p_f.actualmap]['walkable'].body.right

            if maps[p_f.actualmap]['walkable'].body.left > self.body.left:
                self.body.left = maps[p_f.actualmap]['walkable'].body.left

            if maps[p_f.actualmap]['walkable'].body.top > self.body.bottom:
                self.body.bottom = maps[p_f.actualmap]['walkable'].body.top

            if maps[p_f.actualmap]['walkable'].body.bottom < self.body.bottom:
                self.body.bottom = maps[p_f.actualmap]['walkable'].body.bottom

    def attack(self):

        """def find_targets():
            targets = []

            # for creature in creaturesmap[p_f.actualmap]:"""

        if self.normalattackcooldown <= 0 and not self.moveing:
            if p_f.mousepressed:
                p_f.mousepressed = False
                self.attacking = True
                self.animation = 'attack'
                self.normalattackcooldown = p_f.tick * 2
        else:
            self.normalattackcooldown -= 1

        if self.animation == 'breathing':
            self.attacking = False

        if self.skill1cooldown:
            self.skill1cooldown -= 1
            p_f.todraw['icons']['skill1-ability']['body'].height = 50 - self.skill1cooldown
            p_f.todraw['icons']['skill1-ability-number'] = (
            p_f.skillsfont.render(str(round(self.skill1cooldown/p_f.tick, 1)), 1, p_f.pygame.Color(0, 0, 0)),
            (p_f.mapcorners[p_f.actualmap][2] - 150,
             p_f.mapcorners[p_f.actualmap][3] - 48))
            if not self.skill1cooldown:
                p_f.todraw['icons']['skill1-ability-number'] = (
                p_f.skillsfont.render('1', 1, p_f.pygame.Color(33, 250, 180)),
                (p_f.mapcorners[p_f.actualmap][2] - 136,
                 p_f.mapcorners[p_f.actualmap][3] - 48))
        else:

            if p_f.pygame.key.get_pressed()[p_f.pygame.K_1]:
                dict_of_skills.execute(executor=self, activation=self.skill1active,
                                       skilltype=self.skill1, skilllevel=self.level)
                self.skill1cooldown = p_f.tick * dict_of_skills.maindict[self.fraction]['skill 1']['cooldown']

    def level_up(self):
        leveledup = True
        while leveledup:
            leveledup = False
            if self.progress >= self.maxprogress:
                self.level += 1

                leveledup = True

                self.progress -= self.maxprogress
                self.maxprogress = self.level * 100

        self.update_characteristic()

    def rank_up(self):
        self.rank += 1
        self.update_characteristic()

        if self.rank == 3:
            pass


basicplayer = Player((400, 400), (60, 100), 'basic',
                     maxlife=100, maxhealth=100, maxdefense=0, maxdamage=10, maxattackspeed=2, maxcriticalchance=0,
                     maxcriticalmultiplier=1, maxspeed=200, fraction='basic')

player = basicplayer

'''p_f.todraw['things'].append({'body': p_f.pygame.Rect(player.body.x + player.faceing[0]*100 - 100,
                                                             player.body.y + player.faceing[1]*100 - 100,
                                                             player.body.width + abs(player.faceing[0])*player.body.width,
                                                             player.body.height + abs(player.faceing[1])*player.body.height),
                                     'color': p_f.pygame.Color(255, 255, 60)})'''
