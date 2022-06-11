import RPG_group_alpha.parent_file as p_f
from RPG_group_alpha.block.block import Block

maps = [
 0,

 {
  'under walkable': Block(pos=(400, 460), size=(p_f.screenwidth - 800, p_f.screenheight - 460),
                          name='dirt', nick='dirt', loot=('dirt')),
  'walkable': Block(pos=(400, 460), size=(p_f.screenwidth-800, p_f.screenheight-460),
                    name='floor', nick='floor', loot=('wood')),
  'wall': Block(pos=(400, 50), size=(p_f.screenwidth-800, 410),
                name='wood wall inside', nick='wood wall inside', loot=('wood')),
  'left window': Block(pos=(490, 350), size=(60, 60),
                       name='window', nick='window', loot=('glass')),
  'right window': Block(pos=(1090, 350), size=(60, 60),
                        name='window', nick='window', loot=('glass')),
  'exit door': Block(pos=(750, 340), size=(60, 120),
                     name='door', nick='door', loot=('door')),
  'left door': Block(pos=(400, 530), size=(30, 120),
                     name='door', nick='door', loot=('door')),
  'right door': Block(pos=(p_f.screenwidth-430, 530), size=(30, 120),
                      name='door', nick='door', loot=('door'))
 },

 {
  'under walkable': Block(pos=(30, 125), size=(p_f.screenwidth-60, p_f.screenheight-150),
                          name='dirt', nick='dirt', loot=('dirt')),
  'walkable': Block(pos=(30, 125), size=(p_f.screenwidth-60, p_f.screenheight-150),
                    name='grass', nick='grass', loot=('dirt')),
  'home door': Block(pos=(750, 755), size=(60, 120),
                     name='door', nick='door', loot=('door')),
  'path-1': Block(pos=(750, 695), size=(60, 60),
                  name='dirt', nick='dirt', loot=('dirt')),
  'path-2': Block(pos=(690, 515), size=(60, 240),
                  name='dirt', nick='dirt', loot=('dirt')),
  'path-3': Block(pos=(750, 455), size=(60, 120),
                  name='dirt', nick='dirt', loot=('dirt')),
  'path-4': Block(pos=(450, 515), size=(240, 60),
                  name='dirt', nick='dirt', loot=('dirt')),
  'path-5': Block(pos=(210, 575), size=(300, 60),
                  name='dirt', nick='dirt', loot=('dirt')),
  'path-6': Block(pos=(210, 335), size=(60, 240),
                  name='dirt', nick='dirt', loot=('dirt')),
  'path-7': Block(pos=(30, 335), size=(180, 60),
                  name='dirt', nick='dirt', loot=('dirt')),
  'path-8': Block(pos=(810, 455), size=(180, 60),
                  name='dirt', nick='dirt', loot=('dirt')),
  'path-9': Block(pos=(750, 695), size=(60, 60),
                  name='dirt', nick='dirt', loot=('dirt')),
  'path-10': Block(pos=(750, 695), size=(60, 60),
                  name='dirt', nick='dirt', loot=('dirt'))
 }
]

'''
**************************

1 - exit room
2 - forest outside of exit room

**************************
'''