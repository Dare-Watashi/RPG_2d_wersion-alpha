from RPG_group_alpha import parent_file as p_f


''' example of using this module'''
# talk_scene(dialogues[("example1", "example2")])


def talk_scene(dialogue):
    for speaker, text in dialogue:
        p_f.screen.fill((0, 0, 0))
        p_f.pygame.draw.rect(p_f.screen, (120, 120, 120),
                             p_f.pygame.Rect(350, 350, p_f.screenwidth-700, p_f.screenheight-400))

        for line in range(len(text)):
            if speaker % 2 == 1:
                p_f.pygame.draw.rect(p_f.screen, (220, 160, 100),
                                     p_f.pygame.Rect(25, 25, 300, 300))
                p_f.screen.blit(p_f.talkfont.render("Head of 1 speaker", 1, (255, 255, 255, 255)), (25, 275))
            else:
                p_f.pygame.draw.rect(p_f.screen, (100, 160, 220),
                                     p_f.pygame.Rect(p_f.screenwidth - 350, 25, 300, 300))
                p_f.screen.blit(p_f.talkfont.render("Head of 2 speaker", 1, (255, 255, 255, 255)),
                                (p_f.screenwidth - 325, 275))

            p_f.screen.blit(p_f.talkfont.render(str(speaker), 1, (255, 255, 255, 255)), (375, 300))
            label = p_f.talkfont.render(text[line], 1, (255, 255, 255, 255))
            p_f.screen.blit(label, (374, 374+48*line))
            p_f.pygame.display.flip()

        p_f.pygame.time.delay(500)
        while True:
            for ev in p_f.pygame.event.get():
                if ev.type == p_f.pygame.QUIT or p_f.pygame.key.get_pressed()[p_f.pygame.K_ESCAPE]:
                    p_f.running = False
                    exit(0)
            if p_f.pygame.key.get_pressed()[p_f.pygame.K_SPACE]:
                break
