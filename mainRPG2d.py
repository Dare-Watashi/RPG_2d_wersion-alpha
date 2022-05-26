import pygame
import math
from threading import Thread
from random import randint as rr


pygame.init()
myfont = pygame.font.SysFont("Arial", 32)

screen = pygame.display.set_mode((1500, 750))
interrunning = True
tobedrawn = []
touch = pygame.Rect(-1, -1, 1, 1)
touched = False


class Player:
    def __init__(self):
        global interrunning
        self.running = interrunning
        self.body = pygame.Rect(screen.get_width()/2, screen.get_height()/2, 50, 50)
        # pygame.transform.rotate()

        self.normalspeed = 3
        self.sprint = False
        self.sprintspeed = 2

        self.maxlife = 100
        self.life = 100  # life of object
        self.maxwaittorecoverlife = 50
        self.waittorecoverlife = 50
        self.recoverlifeamount = 1

        self.maxhealth = 100
        self.health = 100  # after loosing health (courses and getting ill) life will decrease
        self.maxwaittorecoverhealth = 500
        self.waittorecoverhealth = 500
        self.recoverhealthamount = 1

        self.maxenergy = 100
        self.energy = 100  # used when casted sprint/swimming/climbing/physic attacks
        self.maxwaittorecoverenergy = 25
        self.waittorecoverenergy = 25
        self.recoverenergyamount = 1

        self.maxmana = 100
        self.mana = 100  # used when casted spells
        self.maxwaittorecovermana = 75
        self.waittorecovermana = 75
        self.recovermanaamount = 1

        self.maxdefense = 1
        self.defense = self.maxdefense

        self.punchpower = 5
        self.maxpunchattackwait = 30
        self.punchattackwait = 30

        self.dpsbuff = 0

        self.funcsthread = Thread(target=self.funcs)

        self.level = 1
        self.maxlevelexp = 25
        self.levelexp = 0

        self.isshiftrecovering = False

    def funcs(self):
        global interrunning
        self.running = interrunning

        self.move()
        self.recovery()
        self.shift_recovering()
        self.punch_attack()
        self.take_damage()
        self.dieing()
        self.level_up()

    def take_damage(self):
        for thing in tobedrawn:
            if thing['parent'] != 'player':
                if thing['body'] != 'circle':
                    if thing['body'].colliderect(self.body):
                        self.life -= thing['power'] - self.defense

    def dieing(self):
        global interrunning
        if self.life <= 0:
            interrunning = False
            exit('died')

    def recovery(self):
        # ******* life ********
        if self.waittorecoverlife > 0:
            self.waittorecoverlife -= 1

        if self.life < self.maxlife:
            if self.waittorecoverlife <= 0:
                self.life += self.recoverlifeamount
                self.health -= 0.5
                self.waittorecoverlife = self.maxwaittorecoverlife
                if self.life > self.maxlife:
                    self.life = self.maxlife

        elif self.life >= self.maxlife:
            self.life = self.maxlife
            self.waittorecoverlife = 0

        # ******* health ********
        if self.waittorecoverhealth > 0:
            self.waittorecoverhealth -= 1

        if self.health < self.maxhealth:
            if self.waittorecoverhealth <= 0:
                self.health += self.recoverhealthamount
                self.energy -= 0.5
                self.waittorecoverhealth = self.maxwaittorecoverhealth
                if self.health > self.maxhealth:
                    self.health = self.maxhealth

        elif self.health >= self.maxhealth:
            self.health = self.maxhealth
            self.waittorecoverhealth = 0

        if self.health <= 0:
            self.life += (self.health/2 + 0.01)
            self.health = 0

        # ******* energy ********
        if self.waittorecoverenergy > 0:
            self.waittorecoverenergy -= 1

        if self.energy < self.maxenergy:
            if self.waittorecoverenergy <= 0:
                self.energy += 0
                # self.recoverenergyamount
                self.waittorecoverenergy = self.maxwaittorecoverenergy
                if self.energy > self.maxenergy:
                    self.energy = self.maxenergy

        elif self.energy >= self.maxenergy:
            self.energy = self.maxenergy
            self.waittorecoverenergy = 0

        if self.energy <= 0:
            self.life -= 0.1
            self.energy = 0

        # ******* mana ********
        if self.waittorecovermana > 0:
            self.waittorecovermana -= 1

        if self.mana < self.maxmana:
            if self.waittorecovermana <= 0:
                self.mana += self.recoverenergyamount
                self.energy -= 0.5
                self.waittorecovermana = self.maxwaittorecovermana
                if self.mana > self.maxmana:
                    self.mana = self.maxmana

        elif self.mana >= self.maxmana:
            self.mana = self.maxmana
            self.waittorecovermana = 0

    def shift_recovering(self):
        if pygame.key.get_pressed()[pygame.K_LSHIFT] or pygame.key.get_pressed()[pygame.K_RSHIFT]:
            self.isshiftrecovering = True
            if self.energy > 0:
                self.life += self.recoverlifeamount / 4
                self.energy -= self.recoverenergyamount / 2
                self.mana += self.recovermanaamount / 4
        else:
            self.isshiftrecovering = False

    def move(self):
        actualpositioncheck = (self.body.x, self.body.y)

        if pygame.key.get_pressed()[pygame.K_LCTRL] or pygame.key.get_pressed()[pygame.K_RCTRL]:
            self.sprint = not self.sprint

        if self.sprint:
            speed = self.normalspeed + self.sprintspeed
        else:
            speed = self.normalspeed

        if pygame.key.get_pressed()[pygame.K_w] and\
                (not pygame.key.get_pressed()[pygame.K_LSHIFT] and not pygame.key.get_pressed()[pygame.K_RSHIFT]):
            self.body.y -= speed
            if self.sprint:
                self.energy -= 0.3
        elif pygame.key.get_pressed()[pygame.K_s] and\
                (not pygame.key.get_pressed()[pygame.K_LSHIFT] and not pygame.key.get_pressed()[pygame.K_RSHIFT]):
            self.body.y += speed
            if self.sprint:
                self.energy -= 0.3

        if pygame.key.get_pressed()[pygame.K_a] and\
                (not pygame.key.get_pressed()[pygame.K_LSHIFT] and not pygame.key.get_pressed()[pygame.K_RSHIFT]):
            self.body.x -= speed
            if self.sprint:
                self.energy -= 0.3
        elif pygame.key.get_pressed()[pygame.K_d] and\
                (not pygame.key.get_pressed()[pygame.K_LSHIFT] and not pygame.key.get_pressed()[pygame.K_RSHIFT]):
            self.body.x += speed
            if self.sprint:
                self.energy -= 0.3

        if actualpositioncheck == (self.body.x, self.body.y) and self.energy < self.maxenergy:
            self.energy += 0.4
            if self.energy > self.maxenergy:
                self.energy = self.maxenergy
        else:
            self.waittorecoverenergy = self.maxwaittorecoverenergy

    def punch_attack(self):
        global tobedrawn

        punchpower = self.punchpower + self.dpsbuff

        if self.punchattackwait <= 0 and not self.isshiftrecovering:
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                self.punchattackwait = self.maxpunchattackwait
                self.energy -= 15
                tobedrawn.append({'body': pygame.Rect(self.body.x-35, self.body.y+5, 45, 40),
                                  'time': 3,
                                  'color': (255, 150, 200),
                                  'parent': 'player',
                                  'power': punchpower,
                                  'name': 'spell'})

            elif pygame.key.get_pressed()[pygame.K_UP]:
                self.punchattackwait = self.maxpunchattackwait
                self.energy -= 15
                tobedrawn.append({'body': pygame.Rect(self.body.x+5, self.body.y-35, 40, 45),
                                  'time': 3,
                                  'color': (255, 150, 200),
                                  'parent': 'player',
                                  'power': punchpower,
                                  'name': 'spell'})

            elif pygame.key.get_pressed()[pygame.K_RIGHT]:
                self.punchattackwait = self.maxpunchattackwait
                self.energy -= 15
                tobedrawn.append({'body': pygame.Rect(self.body.x+35, self.body.y+5, 50, 40),
                                  'time': 3,
                                  'color': (255, 150, 200),
                                  'parent': 'player',
                                  'power': punchpower,
                                  'name': 'spell'})

            elif pygame.key.get_pressed()[pygame.K_DOWN]:
                self.punchattackwait = self.maxpunchattackwait
                self.energy -= 15
                tobedrawn.append({'body': pygame.Rect(self.body.x+5, self.body.y+35, 40, 50),
                                  'time': 3,
                                  'color': (255, 150, 200),
                                  'parent': 'player',
                                  'power': punchpower,
                                  'name': 'spell'})

        else:
            self.punchattackwait -= 1

    def level_up(self):
        if self.levelexp >= self.maxlevelexp:
            self.maxlife *= 1.5
            self.maxhealth *= 1.5
            self.maxenergy *= 1.5
            self.mana *= 1.5
            self.defense *= 1.5
            self.punchpower *= 1.5

            self.maxlevelexp *= 1.5
            self.levelexp = 0
            self.level += 1


player = Player()


enemies = []


class Enemy:
    def __init__(self, pos=(0, 0), category='robber'):
        self.body = pygame.Rect(pos, (50, 50))
        self.startcolor = (100, 40, 40)
        self.color = self.startcolor
        self.category = category

        self.maxlife = 100
        self.life = 100
        self.defense = 0

        self.maxspeed = 3
        self.speed = self.maxspeed

        self.punchpower = 5
        self.maxpunchattackwait = 30
        self.punchattackwait = 30

        self.leavingexperience = [4, 2]  # [how much, how much more or less can it be
        self.probablyloot = []

        self.funcsthread = Thread(target=self.funcs)

    def funcs(self):
        if self.category == 'robber':
            if math.fabs(self.body.x - player.body.x) <= 300 and math.fabs(self.body.y - player.body.y) <= 300:
                self.move()

            self.punch_attack()

        self.take_damage()
        self.die()
        # self.appear()

    @staticmethod
    def appear():
        for enemy in range(len(enemies)):
            if type(enemies[enemy]) is int:
                enemies[enemy] -= 1
                if enemies[enemy] <= 0:
                    enemies[enemy] = (Enemy((0, 0), 'robber'), Enemy((1400, 0), 'robber'), Enemy((1400, 600), 'robber'),
                             Enemy((0, 600), 'robber'))[enemy]

    def die(self):
        if self.life <= 0:
            tobedrawn.append({'body': 'circle',
                              'body circle': pygame.Rect((self.body.x, self.body.y), (10, 10)),
                              'size': (((self.body.x+6, self.body.y+6), 7), ((self.body.x+6, self.body.y+6), 15)),
                              'time': 900,
                              'color': ((20, 160, 90), (80, 190, 130)),
                              'parent': 'player',
                              'amount': self.leavingexperience[0] + rr(-self.leavingexperience[1],
                                                                       self.leavingexperience[1]),
                              'name': 'experience particles'})
            enemies[enemies.index(self)] = 600
            if 'taskKillRobber' in tasktable.table:
                tasktable.table['taskKillRobber'].done += 1

    def take_damage(self):
        for thing in tobedrawn:
            if thing['parent'] != 'enemy':
                if thing['body'] != 'circle':
                    if thing['body'].colliderect(self.body):
                        self.life -= thing['power'] - self.defense

    def move(self):
        if self.body.x < player.body.x and player.body.x - self.body.x > 7:
            self.body.x += self.speed
        elif self.body.x > player.body.x and self.body.x - player.body.x > 7:
            self.body.x -= self.speed

        if self.body.y < player.body.y and player.body.y - self.body.y > 7:
            self.body.y += self.speed
        elif self.body.y > player.body.y and self.body.y - player.body.y > 7:
            self.body.y -= self.speed

    def punch_attack(self):
        axes = (0, 0)
        if 0 < self.body.x - player.body.x < 80 and math.fabs(self.body.y - player.body.y) < 10:
            axes = (-1, 0)

        elif -80 < self.body.x - player.body.x < 0 and math.fabs(self.body.y - player.body.y) < 10:
            axes = (1, 0)

        elif 0 < self.body.y - player.body.y < 80 and math.fabs(self.body.x - player.body.x) < 10:
            axes = (0, -1)

        elif -80 < self.body.y - player.body.y < 0 and math.fabs(self.body.x - player.body.x) < 10:
            axes = (0, 1)

        if self.punchattackwait <= 0:
            if axes == (-1, 0):
                self.punchattackwait = self.maxpunchattackwait
                tobedrawn.append({'body': pygame.Rect(self.body.x-35, self.body.y+5, 45, 40),
                                  'time': 3,
                                  'color': (200, 110, 160),
                                  'parent': 'enemy',
                                  'name': 'spell',
                                  'power': self.punchpower})

            elif axes == (1, 0):
                self.punchattackwait = self.maxpunchattackwait
                tobedrawn.append({'body': pygame.Rect(self.body.x+35, self.body.y+5, 45, 40),
                                  'time': 3,
                                  'color': (200, 110, 160),
                                  'parent': 'enemy',
                                  'name': 'spell',
                                  'power': self.punchpower})

            elif axes == (0, -1):
                self.punchattackwait = self.maxpunchattackwait
                tobedrawn.append({'body': pygame.Rect(self.body.x+5, self.body.y-35, 40, 45),
                                  'time': 3,
                                  'color': (200, 110, 160),
                                  'parent': 'enemy',
                                  'name': 'spell',
                                  'power': self.punchpower})

            elif axes == (0, 1):
                self.punchattackwait = self.maxpunchattackwait
                tobedrawn.append({'body': pygame.Rect(self.body.x+5, self.body.y+35, 40, 45),
                                  'time': 3,
                                  'color': (200, 110, 160),
                                  'parent': 'enemy',
                                  'name': 'spell',
                                  'power': self.punchpower})

        else:
            self.punchattackwait -= 1


class TaskTable:
    def __init__(self):
        self.opened = False
        self.maxopenclosewait = 10
        self.openclosewait = 0
        self.bodyclosed = pygame.Rect(screen.get_width()-100, 25, 50, 50)
        self.bodyclosedcolor = (230, 130, 130)
        self.bodyopened = pygame.Rect(400, 50, 800, 600)
        self.bodyopenedcolor = (220, 125, 125)
        self.body = self.bodyclosed
        self.color = self.bodyclosedcolor

        self.table = {}

    def funcs(self):
        self.open_close()
        self.complete_task()

    def open_close(self):
        if pygame.key.get_pressed()[pygame.K_t] or (not self.opened and touch.colliderect(self.bodyclosed)):
            if self.openclosewait <= 0:
                self.opened = not self.opened
                self.openclosewait = self.maxopenclosewait
                if self.opened:
                    self.body = self.bodyopened
                    self.color = self.bodyopenedcolor
                else:
                    self.body = self.bodyclosed
                    self.color = self.bodyclosedcolor

        if self.openclosewait <= 0:
            if pygame.key.get_pressed()[pygame.K_ESCAPE] and self.opened:
                self.opened = False
                self.openclosewait = self.maxopenclosewait

        if self.openclosewait > 0:
            self.openclosewait -= 1

    def printing(self):
        if self.opened:
            for key in self.table:
                if key == 'taskKillRobber':
                    pygame.draw.rect(screen, (self.bodyopenedcolor[0] - 50, self.bodyopenedcolor[1] - 50,
                                              self.bodyopenedcolor[2] - 50), pygame.Rect(self.bodyopened.x + 25,
                                                                                         self.bodyopened.y + 25,
                                                                                         self.bodyopened.width - 50,
                                                                                         150))

                    label = myfont.render(f'Kill {self.table[key].amount} robbers', True, (255, 255, 255))
                    screen.blit(label, (self.bodyopened.x + 50, self.bodyopened.y + 50))
                    pygame.draw.rect(
                        screen, (50, 50, 150),
                        pygame.Rect(self.bodyopened.x + 50, self.bodyopened.y + 100,
                                    self.bodyopened.width - 200, 15))
                    pygame.draw.rect(
                        screen, (150, 150, 250),
                        pygame.Rect(self.bodyopened.x + 50, self.bodyopened.y + 105,
                                    self.table[key].done*((self.bodyopened.width-200)/self.table[key].amount), 5))

    @staticmethod
    def complete_task():
        if tasktable.table:
            try:
                for task in tasktable.table:
                    if tasktable.table[task].amount - tasktable.table[task].done <= 0:
                        print('done')
                        tasktable.table.__delitem__(task)
            except:
                pass

    class Task:
        def __init__(self, typ='kill', target='robber', amount=4):
            self.type = typ  # 'kill' / 'collect' / 'go'
            self.target = target  # 'robber' / 'mint' / 'someone'
            self.amount = amount  # only if type != 'go'
            self.done = 0


tasktable = TaskTable()
tasktable.table['taskKillRobber'] = tasktable.Task('kill', 'robber', 4)

enemies.extend([Enemy((0, 0), 'robber'), Enemy((1400, 0), 'robber'), Enemy((1400, 600), 'robber'),
                Enemy((0, 600), 'robber')])

while interrunning:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT or (ev.type == pygame.K_ESCAPE and not tasktable.opened):
            interrunning = False
        if ev.type == pygame.MOUSEBUTTONDOWN:
            touch.x, touch.y = pygame.mouse.get_pos()
            touched = True
        elif ev.type == pygame.MOUSEBUTTONUP:
            touched = False

    if pygame.key.get_pressed()[pygame.K_ESCAPE] and not tasktable.opened:
        interrunning = False

    # try:
    if True:
        screen.fill('black')

        if not tasktable.opened:
            if not player.funcsthread.is_alive():
                player.funcsthread = Thread(target=player.funcs)
                player.funcsthread.run()
            for enemy in enemies:
                if type(enemy) is not int:
                    if not enemy.funcsthread.is_alive():
                        enemy.funcsthread = Thread(target=enemy.funcs)
                        enemy.funcsthread.run()
            Enemy().appear()

        def draw():
            global player, enemies, tobedrawn, tasktable

            pygame.draw.rect(screen, 'white', player.body)
            for enemy in enemies:
                if type(enemy) is not int:
                    pygame.draw.rect(screen, enemy.color, enemy.body)

            for thing in tobedrawn:
                if thing['body'] == 'circle':
                    pygame.draw.circle(screen, thing['color'][1], thing['size'][1][0], thing['size'][1][1])
                    pygame.draw.circle(screen, thing['color'][0], thing['size'][0][0], thing['size'][0][1])
                    if not tasktable.opened:
                        thing['time'] -= 1
                    if thing['name'] == 'experience particles' and thing['body circle'].colliderect(player.body):
                        player.levelexp += thing['amount']
                        thing['time'] = 0
                else:
                    pygame.draw.rect(screen, thing['color'], thing['body'])
                    if not tasktable.opened:
                        thing['time'] -= 1

                if thing['name'] == 'spell' and not tasktable.opened:
                    # if thing['body'].collidelist(enemies):
                    pass

                if not thing['time']:
                    tobedrawn.remove(thing)

            # try:
            if True:
                for enemy in enemies:
                    if type(enemy) is not int:
                        pygame.draw.rect(screen, 'red', pygame.Rect(enemy.body.x - 25, enemy.body.y - 15,
                                                                    int(enemy.life), 10))
            # except:
            #    pass

            pygame.draw.rect(screen, 'red', pygame.Rect(10, 10,
                                                        int((player.life/(player.maxlife/100)) * 1.5), 15))
            pygame.draw.rect(screen, 'green', pygame.Rect(10, 30,
                                                          int((player.health/(player.maxhealth/100)) * 1.5), 15))
            pygame.draw.rect(screen, 'yellow', pygame.Rect(10, 50,
                                                           int((player.energy/(player.maxenergy/100)) * 1.5), 15))
            pygame.draw.rect(screen, 'blue', pygame.Rect(10, 70,
                                                         int((player.mana/(player.maxmana/100)) * 1.5), 15))

            pygame.draw.rect(screen, tasktable.color, tasktable.body)
            tasktable.printing()

        Thread(target=draw).run()

        tasktable.funcs()

        pygame.display.flip()
        pygame.time.Clock().tick(35)

    # except:
    #    pass
