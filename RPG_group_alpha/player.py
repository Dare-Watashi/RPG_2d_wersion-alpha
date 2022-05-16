import parent_file as p_f


class Player:
    def __init__(self, place, size, rotation=0):
        self.normalposition = place
        self.position = self.normalposition
        self.normalscale = size
        self.scale = self.normalscale
        self.normalrotation = rotation
        self.rotation = self.normalrotation

        self.body = p_f.pygame.Rect(self.position, self.scale)
        self.normalcolor = p_f.pygame.Color(200, 150, 160, 255)
        self.color = self.normalcolor

    def move(self):
        if p_f.pygame.key.get_pressed()[p_f.pygame.K_d]:



player = Player((400, 400), (50, 100), 45)
