import parent_file as p_f
from player import player
import world

world.fillmap()


while p_f.running:
    for ev in p_f.pygame.event.get():
        if ev.type == p_f.pygame.QUIT or p_f.pygame.key.get_pressed()[p_f.pygame.K_ESCAPE]:
            p_f.running = False
        elif ev.type == p_f.pygame.MOUSEBUTTONDOWN:
            pass
        elif ev.type == p_f.pygame.MOUSEBUTTONUP:
            pass

    player.move()

    p_f.screen.fill((0, 0, 0, 0))

    world.drawworld()

    p_f.pygame.draw.rect(p_f.screen, player.normalcolor, player.body)
    p_f.pygame.time.Clock().tick(25)
    p_f.pygame.display.flip()
