from RPG_group_alpha import parent_file as p_f

img = p_f.pygame.image.load(r'/home/patryk/PycharmProjects/RPG_2d_wersion-alpha/RPG_group_alpha/textures/player_weapons1-2.png')

playeranimation = {
    'breathing': [p_f.pygame.transform.scale(img.subsurface(p_f.pygame.Rect(0*24, 0, 24, 24)), (100, 100)),
                  p_f.pygame.transform.scale(img.subsurface(p_f.pygame.Rect(1 * 24, 0, 24, 24)), (100, 100))],

    'attack': [p_f.pygame.transform.scale(img.subsurface(p_f.pygame.Rect(2 * 24, 0, 24, 24)), (100, 100)),
               p_f.pygame.transform.scale(img.subsurface(p_f.pygame.Rect(3 * 24, 0, 24, 24)), (100, 100)),
               p_f.pygame.transform.scale(img.subsurface(p_f.pygame.Rect(4 * 24, 0, 24, 24)), (100, 100)),
               p_f.pygame.transform.scale(img.subsurface(p_f.pygame.Rect(5 * 24, 0, 24, 24)), (100, 100))],

    'skill1active': [p_f.pygame.transform.scale(img.subsurface(p_f.pygame.Rect(4 * 24, 0, 24, 24)), (100, 100))]
}


spearanimation = {
    'breathing': [p_f.pygame.transform.scale(img.subsurface(p_f.pygame.Rect(0 * 24, 24, 24, 24)), (100, 100)),
                  p_f.pygame.transform.scale(img.subsurface(p_f.pygame.Rect(1 * 24, 24, 24, 24)), (100, 100))],

    'attack': [p_f.pygame.transform.scale(img.subsurface(p_f.pygame.Rect(2 * 24, 24, 24, 24)), (100, 100)),
               p_f.pygame.transform.scale(img.subsurface(p_f.pygame.Rect(3 * 24, 24, 24, 24)), (100, 100)),
               p_f.pygame.transform.scale(img.subsurface(p_f.pygame.Rect(4 * 24, 24, 24, 24)), (100, 100)),
               p_f.pygame.transform.scale(img.subsurface(p_f.pygame.Rect(5 * 24, 24, 24, 24)), (100, 100))],

    'skill1active': [p_f.pygame.transform.scale(img.subsurface(p_f.pygame.Rect(4 * 24, 24, 24, 24)), (100, 100))]

}


knifeanimation = {
    'breathing': [p_f.pygame.transform.scale(img.subsurface(p_f.pygame.Rect(0 * 24, 48, 24, 24)), (100, 100)),
                  p_f.pygame.transform.scale(img.subsurface(p_f.pygame.Rect(1 * 24, 48, 24, 24)), (100, 100))],

    'attack': [p_f.pygame.transform.scale(img.subsurface(p_f.pygame.Rect(2 * 24, 48, 24, 24)), (100, 100)),
               p_f.pygame.transform.scale(img.subsurface(p_f.pygame.Rect(3 * 24, 48, 24, 24)), (100, 100)),
               p_f.pygame.transform.scale(img.subsurface(p_f.pygame.Rect(4 * 24, 48, 24, 24)), (100, 100)),
               p_f.pygame.transform.scale(img.subsurface(p_f.pygame.Rect(5 * 24, 48, 24, 24)), (100, 100))],

    'skill1active': [p_f.pygame.transform.scale(img.subsurface(p_f.pygame.Rect(4 * 24, 48, 24, 24)), (100, 100))]
}


delays = {'playeranimation breathing': 333,
          'playeranimation attack': 200,
          'playeranimation skill1active': 200,
          'spearanimation breathing': 333,
          'spearanimation attack': 200,
          'spearanimation skill1active': 200,
          'knifeanimation breathing': 333,
          'knifeanimation attack': 200,
          'knifeanimation skill1active': 200}
