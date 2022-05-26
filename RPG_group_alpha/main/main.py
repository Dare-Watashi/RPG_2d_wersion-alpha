from RPG_group_alpha import parent_file as p_f
from RPG_group_alpha.interactions.interactions import Interaction
from RPG_group_alpha.main import drawing

'''*************** calling starting threads ***************'''

interactionobject = Interaction()


'''*************** main loop ***************'''

while p_f.running:
    for ev in p_f.pygame.event.get():
        if ev.type == p_f.pygame.QUIT or p_f.pygame.key.get_pressed()[p_f.pygame.K_ESCAPE]:
            p_f.running = False

    drawing.draw_screen()

    p_f.clock.tick(p_f.tick)
    p_f.pygame.display.flip()
