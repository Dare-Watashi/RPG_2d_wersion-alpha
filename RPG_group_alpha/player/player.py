from RPG_group_alpha import parent_file as p_f
from RPG_group_alpha.world.world_maps import maps


class Player:
    def __init__(self, place, size):
        self.normalscale = size
        self.scale = self.normalscale

        self.body = p_f.pygame.Rect(place, self.scale)
        self.normalcolor = p_f.pygame.Color(200, 150, 160, 255)
        self.color = self.normalcolor

        self.runspeed = 250
        self.walkspeed = 150
        self.speed = self.walkspeed

        self.functionsthread = p_f.threadCenter.append(self.calling_functions)

    def calling_functions(self):
        while p_f.running:
            self.move()

            p_f.clock.tick(p_f.tick)

    def move(self):
        if p_f.pygame.key.get_pressed()[p_f.pygame.K_LSHIFT]:
            self.speed = p_f.mps(self.walkspeed)

        if p_f.pygame.key.get_pressed()[p_f.pygame.K_LCTRL]:
            self.speed = p_f.mps(self.runspeed)

        if p_f.pygame.key.get_pressed()[p_f.pygame.K_d]\
                and maps[p_f.actualmap]['walkable'].body.right > self.body.right + (self.speed / p_f.clock.get_fps() + 0.01)/2:
            if p_f.pygame.key.get_pressed()[p_f.pygame.K_w] or p_f.pygame.key.get_pressed()[p_f.pygame.K_s]:
                self.body.x += (self.speed / p_f.clock.get_fps() + 0.01) * p_f.numpy.sin(45)
            else:
                self.body.x += self.speed / p_f.clock.get_fps() + 0.01

        if p_f.pygame.key.get_pressed()[p_f.pygame.K_a]\
                and maps[p_f.actualmap]['walkable'].body.left < self.body.left - (self.speed / p_f.clock.get_fps() + 0.01)/2:
            if p_f.pygame.key.get_pressed()[p_f.pygame.K_w] or p_f.pygame.key.get_pressed()[p_f.pygame.K_s]:
                self.body.x -= (self.speed / p_f.clock.get_fps() + 0.01) * p_f.numpy.sin(45)
            else:
                self.body.x -= self.speed / p_f.clock.get_fps() + 0.01

        if p_f.pygame.key.get_pressed()[p_f.pygame.K_w]\
                and maps[p_f.actualmap]['walkable'].body.top < self.body.bottom - (self.speed / p_f.clock.get_fps() + 0.01)/2:
            if p_f.pygame.key.get_pressed()[p_f.pygame.K_a] or p_f.pygame.key.get_pressed()[p_f.pygame.K_d]:
                self.body.y -= (self.speed / p_f.clock.get_fps() + 0.01) * p_f.numpy.sin(45)
            else:
                self.body.y -= self.speed / p_f.clock.get_fps() + 0.01

        if p_f.pygame.key.get_pressed()[p_f.pygame.K_s]\
                and maps[p_f.actualmap]['walkable'].body.bottom > self.body.bottom + (self.speed / p_f.clock.get_fps() + 0.01)/2:
            if p_f.pygame.key.get_pressed()[p_f.pygame.K_a] or p_f.pygame.key.get_pressed()[p_f.pygame.K_d]:
                self.body.y += (self.speed / p_f.clock.get_fps() + 0.01) * p_f.numpy.sin(45)
            else:
                self.body.y += self.speed / p_f.clock.get_fps() + 0.01

        p_f.pygame.time.delay(20)


player = Player((400, 400), (60, 100))
