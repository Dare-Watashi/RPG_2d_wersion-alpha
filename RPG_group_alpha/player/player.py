from RPG_group_alpha import parent_file as p_f
from RPG_group_alpha.world.world_maps import maps
from RPG_group_alpha.player.elements_classes import elements
from RPG_group_alpha.player import dict_of_attacks_and_skills as dict_of_skills
from RPG_group_alpha.player.menu import while_menu_opened


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
        self.attackspeed = self.maxattackspeed * (1 + (1 - self.element.multipliers['attack speed']))
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
        self.weaponrange = 50

        self.normalattackcollisioner = p_f.pygame.Rect(
            self.body.x if self.faceing[0] >= 0 else self.body.x - self.weaponrange,
            self.body.y if self.faceing[1] >= 0 else self.body.y - self.weaponrange,
            self.body.width if self.faceing[0] == 0 else self.body.width + self.weaponrange,
            self.body.height if self.faceing[1] == 0 else self.body.height + self.weaponrange
        )

        self.moveing = False
        self.attacking = False
        self.normalattackcooldown = p_f.tick * 2 * self.attackspeed

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
        p_f.pygame.time.delay(1000)
        while p_f.running:
            self.open_player_menu()

            self.move()
            self.attack()
            self.level_up()

            p_f.clock.tick(p_f.tick)

        p_f.threadCenter.sleep()

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
        self.normalattackcollisioner = p_f.pygame.Rect(
            self.body.x if self.faceing[0] >= 0 else self.body.x - self.weaponrange,
            self.body.y if self.faceing[1] >= 0 else self.body.y - self.weaponrange,
            self.body.width if self.faceing[0] == 0 else self.body.width + self.weaponrange,
            self.body.height if self.faceing[1] == 0 else self.body.height + self.weaponrange)

        if self.normalattackcooldown <= 0 and not self.moveing:
            if p_f.mousepressed:
                p_f.mousepressed = False
                self.attacking = True
                self.animation = 'attack'

                dict_of_skills.hurt_targets_in_range(self, self.damage, exceptors=[])

                self.normalattackcooldown = p_f.tick * 2 * (1 + (1 - self.element.multipliers['attack speed']))
        else:
            self.normalattackcooldown -= 1

        if self.animation == 'breathing':
            self.attacking = False

        if self.skill1cooldown:
            self.skill1cooldown -= 1
            p_f.todraw['icons']['skill1-ability']['body'].height = 50 - self.skill1cooldown
            p_f.todraw['icons']['skill1-ability-number'] = (
            p_f.skillsfont.render(str(round(self.skill1cooldown/p_f.tick, 1)), 1, p_f.pygame.Color(0, 0, 0)),
            (p_f.screenwidth - 198,
             p_f.screenheight - 96))
            if not self.skill1cooldown:
                p_f.todraw['icons']['skill1-ability-number'] = (
                p_f.skillsfont.render('1', 1, p_f.pygame.Color(33, 250, 180)),
                (p_f.screenwidth - 186,
                 p_f.screenheight - 96))
        else:

            if p_f.pygame.key.get_pressed()[p_f.pygame.K_1]:
                dict_of_skills.execute(executor=self, activation=self.skill1active,
                                       skilltype=self.skill1, skilllevel=self.level, skillnumber="skill 1")
                self.skill1cooldown = p_f.tick * dict_of_skills.maindict[self.fraction]\
                    ['skill 1']['cooldown'] * (1 + (1 - self.element.multipliers['attack speed']))

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

    def open_player_menu(self):
        p_f.pygame.init()

        if not p_f.playerisfighting and not p_f.talkingscene:
            if p_f.pygame.key.get_pressed()[p_f.pygame.K_c]:
                p_f.playersmenuopened = True
                while_menu_opened()
        elif p_f.playerisfighting:
            if p_f.pygame.key.get_pressed()[p_f.pygame.K_c]:
                p_f.todraw["icons"]["can't open the menu while fighting"] = [
                    p_f.objectsfont.render(str("can't open the menu while fighting"), 1, p_f.pygame.Color('white')),
                    (p_f.screenwidth//2-150, p_f.screenheight-200), p_f.tick*2]


basicplayer = Player((400, 400), (60, 100), 'basic',
                     maxlife=100, maxhealth=100, maxdefense=0, maxdamage=10, maxattackspeed=2, maxcriticalchance=0,
                     maxcriticalmultiplier=1, maxspeed=200, fraction='basic')

player = basicplayer
