from RPG_group_alpha import parent_file as p_f
from RPG_group_alpha.world.world_maps import maps


class Player:
    def __init__(self, place, size, rotation=0):
        self.normalscale = size
        self.scale = self.normalscale
        self.normalrotation = rotation
        self.rotation = self.normalrotation

        self.body = p_f.pygame.Rect(place, self.scale)
        self.normalcolor = p_f.pygame.Color(200, 150, 160, 255)
        self.color = self.normalcolor

        self.runspeed = 10
        self.walkspeed = 6
        self.speed = self.walkspeed

        self.functionsthread = p_f.threadCenter.append(self.calling_functions)

    def calling_functions(self):
        while p_f.running:
            self.move()

            p_f.clock.tick(p_f.tick)

    def move(self):
        if p_f.pygame.key.get_pressed()[p_f.pygame.K_LSHIFT]:
            self.speed = self.walkspeed

        if p_f.pygame.key.get_pressed()[p_f.pygame.K_LCTRL]:
            self.speed = self.runspeed

        if p_f.pygame.key.get_pressed()[p_f.pygame.K_d]\
                and maps[p_f.actualmap]['walkable'].body.right > self.body.right + self.speed/2:
            self.body.x += self.speed

        if p_f.pygame.key.get_pressed()[p_f.pygame.K_a]\
                and maps[p_f.actualmap]['walkable'].body.left < self.body.left - self.speed/2:
            self.body.x -= self.speed

        if p_f.pygame.key.get_pressed()[p_f.pygame.K_w]\
                and maps[p_f.actualmap]['walkable'].body.top < self.body.bottom - self.speed/2:
            self.body.y -= self.speed

        if p_f.pygame.key.get_pressed()[p_f.pygame.K_s]\
                and maps[p_f.actualmap]['walkable'].body.bottom > self.body.bottom + self.speed/2:
            self.body.y += self.speed

        p_f.pygame.time.delay(20)


player = Player((400, 400), (40, 100))
