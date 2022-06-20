from RPG_group_alpha import parent_file as p_f
from RPG_group_alpha.world import world_maps


species = ['human', 'wolf', 'rabbit', 'horse']

target = None


class Creature:
    def __init__(self, position, size, level, life, speed, color, character):

        self.body = p_f.pygame.Rect(position, size)
        self.level = level
        self.life = life
        self.speed = speed
        self.color = p_f.pygame.Color(color[0], color[1], color[2]),
        self.character = character

        self.moveing = False
        self.destination = self.body.x, self.body.y

        self.fighting = False
        self.target = None

    def move_to(self, gox, goy):
        if not self.moveing and not self.fighting:
            self.destination = gox, goy
            self.moveing = True

        if self.fighting:
            self.destination = gox, goy
            self.moveing = True

        if self.body.x + self.speed / (p_f.clock.get_fps() + 0.01) < self.destination[0]:
            if self.body.y + self.speed / (p_f.clock.get_fps() + 0.01) < self.destination[1] < \
                    self.body.y + self.speed / (p_f.clock.get_fps() + 0.01):
                self.body.x += self.speed / (p_f.clock.get_fps() + 0.01) * p_f.numpy.sin(45)
            else:
                self.body.x += self.speed / (p_f.clock.get_fps() + 0.01)
        elif self.body.x - self.speed / (p_f.clock.get_fps() + 0.01) > self.destination[0]:
            if self.body.y + self.speed / (p_f.clock.get_fps() + 0.01) < self.destination[1] < \
                    self.body.y + self.speed / (p_f.clock.get_fps() + 0.01):
                self.body.x -= self.speed / (p_f.clock.get_fps() + 0.01) * p_f.numpy.sin(45)
            else:
                self.body.x -= self.speed / (p_f.clock.get_fps() + 0.01)

        if self.body.y + self.speed / (p_f.clock.get_fps() + 0.01) < self.destination[1]:
            if self.body.x + self.speed / (p_f.clock.get_fps() + 0.01) < self.destination[0] < \
                    self.body.x + self.speed / (p_f.clock.get_fps() + 0.01):
                self.body.y += self.speed / (p_f.clock.get_fps() + 0.01) * p_f.numpy.sin(45)
            else:
                self.body.y += self.speed / (p_f.clock.get_fps() + 0.01)
        elif self.body.y - self.speed / (p_f.clock.get_fps() + 0.01) > self.destination[1]:
            if self.body.x + self.speed / (p_f.clock.get_fps() + 0.01) < self.destination[0] < \
                    self.body.x + self.speed / (p_f.clock.get_fps() + 0.01):
                self.body.y -= self.speed / (p_f.clock.get_fps() + 0.01) * p_f.numpy.sin(45)
            else:
                self.body.y -= self.speed / (p_f.clock.get_fps() + 0.01)

        if self.body.x + self.speed / (p_f.clock.get_fps() + 0.01) > self.destination[0] > \
                self.body.x - self.speed / (p_f.clock.get_fps() + 0.01) and \
                self.body.y + self.speed / (p_f.clock.get_fps() + 0.01) > self.destination[1] > \
                self.body.y - self.speed / (p_f.clock.get_fps() + 0.01):
            self.moveing = False


class Human(Creature):
    def __init__(self, position, level, color, character):
        super(Human, self).__init__(
            position=position,
            size=(60, 100),
            level=level,
            life=100*level,
            speed=150,
            color=p_f.pygame.Color(color[0], color[1], color[2]),
            character=character
        )


class Robber(Human):
    def __init__(self, position, level):
        super(Robber, self).__init__(
            position=position,
            level=level,
            color=p_f.pygame.Color(15, 7, 5),
            character='aggressive'
        )
        self.damage = 10 * self.level

    def update(self):
        if not self.fighting:
            self.move_to(
                p_f.randint(int(world_maps.maps[p_f.actualmap]['walkable'].body.left+self.body.width/2),
                            int(world_maps.maps[p_f.actualmap]['walkable'].body.right-self.body.width*1.5)),
                p_f.randint(int(world_maps.maps[p_f.actualmap]['walkable'].body.top + self.body.height/2),
                            int(world_maps.maps[p_f.actualmap]['walkable'].body.bottom - self.body.height*1.5))
                         )
        else:
            if self.target is not None:
                self.move_to(self.target.body.x, self.target.body.y)

        if target is not None:
            if abs(self.body.x - target.body.x) < 300 and abs(self.body.y - target.body.y) < 300:
                self.target = target
                self.fighting = True
