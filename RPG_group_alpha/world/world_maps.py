import RPG_group_alpha.parent_file as p_f
from RPG_group_alpha.block.block import Block

maps = [
 0,
 {
  'walkable': Block(pos=(400, 460), size=(p_f.screenwidth-800, p_f.screenheight-460), name='floor', nick='floor', loot=('wood')),
  'wall': Block(pos=(400, 50), size=(p_f.screenwidth-800, 410), name='wood wall', nick='wood wall', loot=('wood')),
  'left window': Block(pos=(490, 350), size=(60, 60), name='window', nick='window', loot=('glass')),
  'right window': Block(pos=(1090, 350), size=(60, 60), name='window', nick='window', loot=('glass')),
  'exit door': Block(pos=(750, 340), size=(60, 120), name='door', nick='door', loot=('door')),
  'left door': Block(pos=(400, 530), size=(30, 120), name='door', nick='door', loot=('door')),
  'right door': Block(pos=(p_f.screenwidth-430, 530), size=(30, 120), name='door', nick='door', loot=('door'))
 },
 {
  'walkable': Block(pos=(25, 125), size=(p_f.screenwidth-50, p_f.screenheight-150), name='dirt', nick='dirt', loot=('dirt')),
  'home door': Block(pos=(750, p_f.screenheight-145), size=(60, 120), name='door', nick='door', loot=('door'))
 }
]

'''
**************************

1 - exit room
2 - forest outside of exit room

**************************
'''