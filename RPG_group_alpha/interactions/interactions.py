from RPG_group_alpha import parent_file as p_f
from RPG_group_alpha.world.world_maps import maps
from RPG_group_alpha.player.player import player
from RPG_group_alpha.main import drawing


class Interaction:
    def __init__(self):
        self.mapchanges = {0: 0,
                           1: {"exit door": 2},
                           2: {"home door": 1}}

        self.interactionsthread = p_f.threadCenter.append(self.check_interactions)

    def check_interactions(self):
        p_f.pygame.init()
        while p_f.running:
            '''*************** executing and removing objects to draw ***************'''

            if drawing.todraw.__len__() > 0:
                for thing in drawing.todraw:
                    if not player.body.colliderect(maps[thing['map']][thing['parent']].body)\
                            or thing['map'] != p_f.actualmap:
                        drawing.todraw.remove(thing)
                    else:
                        if 'action' in thing.keys():
                            if thing['action'] == self.change_map and p_f.pygame.key.get_pressed()[p_f.pygame.K_SPACE]:
                                thing['action'](thing['args'])

            '''*************** map change ***************'''

            try:
                for interactiveobject in self.mapchanges[p_f.actualmap]:
                    if player.body.colliderect(maps[p_f.actualmap][interactiveobject].body):
                        doorrect = p_f.pygame.Rect(maps[p_f.actualmap][interactiveobject].body.x +
                                                   maps[p_f.actualmap][interactiveobject].body.size[0],
                                                   maps[p_f.actualmap][interactiveobject].body.y +
                                                   maps[p_f.actualmap][interactiveobject].body.size[1]//2, 50, 25)
                        dictionary = {'parent': interactiveobject, 'map': p_f.actualmap,
                                      'color': p_f.pygame.Color(100, 100, 100, 150),
                                      'body': doorrect, 'text': 'door', 'action': self.change_map,
                                      'args': self.mapchanges[p_f.actualmap][interactiveobject]}
                        if dictionary not in drawing.todraw:
                            drawing.todraw.append(dictionary)
            except:
                pass

    def change_map(self, nextmap):
        lastmap = p_f.actualmap
        p_f.actualmap = nextmap

        player.body.x = maps[p_f.actualmap]["walkable"].position[0]\
                        + maps[p_f.actualmap]["walkable"].size[0]/2
        player.body.y = maps[p_f.actualmap]["walkable"].position[1]\
                        + maps[p_f.actualmap]["walkable"].size[1]/2
