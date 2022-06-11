from RPG_group_alpha import parent_file as p_f

# when player's strength is 50
durabilitytable = {'weed': 5,
                   'dirt': 250,
                   'glass': 400,
                   'wood': 800,
                   'door': 1000,
                   'stone': 2000}

typesofblocks = {
    "type name": {"material": bool,
                  "destroyable": bool,
                  "collectable": bool},

    "air": {"material": False,
            "destroyable": False,
            "collectable": True},

    "door": {"material": True,
             "destroyable": True,
             "collectable": True},

    "glass": {"material": True,
              "destroyable": True,
              "collectable": True},

    "ground": {"material": True,
               "destroyable": True,
               "collectable": True},

    "weed": {"material": True,
             "destroyable": True,
             "collectable": True},

    "wood": {"material": True,
             "destroyable": True,
             "collectable": True}
}

blocksinfo = {
    "block name": {"type": "type name",
                   "color": p_f.pygame.Color,
                   "durability": int,
                   "interactive": bool,
                   "colliding": bool},

    "dirt": {"type": "ground",
             "color": p_f.pygame.Color(120, 40, 30, 255),
             "durability": durabilitytable['dirt'],
             "interactive": False,
             "colliding": False},

    "door": {"type": "door",
             "color": p_f.pygame.Color(96, 36, 28, 255),
             "durability": durabilitytable['door'],
             "interactive": True,
             "colliding": False},

    "floor": {"type": "ground",
              "color": p_f.pygame.Color(240, 90, 68, 255),
              "durability": durabilitytable['wood'],
              "interactive": False,
              "colliding": False},

    "glass": {"type": "glass",
              "color": p_f.pygame.Color(150, 150, 255, 150),
              "durability": durabilitytable['glass'],
              "interactive": False,
              "colliding": False},

    "grass": {"type": "weed",
              "color": p_f.pygame.Color(71, 143, 86, 200),
              "durability": durabilitytable['weed'],
              "interactive": False,
              "colliding": False},

    "stone wall inside": {"type": "ground",
                          "color": p_f.pygame.Color(150, 118, 120, 255),
                          "durability": durabilitytable['stone'],
                          "interactive": False,
                          "colliding": False},

    "stone wall outside": {"type": "ground",
                           "color": p_f.pygame.Color(150, 118, 120, 255),
                           "durability": durabilitytable['stone'],
                           "interactive": False,
                           "colliding": True},

    "window": {"type": "glass",
               "color": p_f.pygame.Color(150, 150, 255, 150),
               "durability": durabilitytable['glass'],
               "interactive": False,
               "colliding": False},

    "wood wall inside": {"type": "wood",
                         "color": p_f.pygame.Color(120, 45, 34, 255),
                         "durability": durabilitytable['wood'],
                         "interactive": False,
                         "colliding": False},

    "wood wall outside": {"type": "wood",
                          "color": p_f.pygame.Color(120, 45, 34, 255),
                          "durability": durabilitytable['wood'],
                          "interactive": False,
                          "colliding": True}
}


class Block:
    def __init__(self, pos, size, name, nick, loot=None):
        self.position = pos
        self.size = size
        self.name = name
        self.nick = nick
        self.loot = loot
        self.color = blocksinfo[self.name]["color"]
        self.body = p_f.pygame.Rect(self.position, self.size)
