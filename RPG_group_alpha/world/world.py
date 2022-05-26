from RPG_group_alpha import parent_file as p_f
from RPG_group_alpha.world.world_maps import maps

screenwidth, screenheight = p_f.screenwidth, p_f.screenheight


def draw_map():
    amap = maps[p_f.actualmap]

    for value in amap:
        if value != "":
            p_f.pygame.draw.rect(p_f.screen, amap[value].color, amap[value].body)

