from RPG_group_alpha import parent_file as p_f
from RPG_group_alpha.textures import division_and_organisation as dao


class Menu:
    def __init__(self):
        self.exiter = p_f.pygame.Rect(40, 40, 50, 50)

        self.character = p_f.pygame.transform.scale(dao.img.subsurface(p_f.pygame.Rect(0*24, 0, 24, 24)), (500, 500))
        self.experiencebar = None


menu = Menu()


def while_menu_opened():
    while True:
        if p_f.mousepressed:
            if p_f.pygame.Rect(p_f.pygame.mouse.get_pos(), (1, 1)).colliderect(menu.exiter):
                p_f.playersmenuopened = False
                break
        if not p_f.running:
            exit(0)

        p_f.screen.fill('black')
        p_f.screen.blit(menu.character, (700, 300))
        p_f.pygame.draw.rect(p_f.screen, "white", menu.exiter)
        p_f.pygame.display.flip()
