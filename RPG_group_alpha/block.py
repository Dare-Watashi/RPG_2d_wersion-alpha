import parent_file as p_f

typesofblocks = {
    "type name": {"material": bool,
                  "destroyable": bool,
                  "collectable": bool,
                  "interactive": bool},

    "ground": {"material": True,
               "destroyable": True,
               "collectable": True,
               "interactive": False},

    "air": {"material": False,
            "destroyable": False,
            "collectable": False,
            "interactive": False}
}

blocksinfo = {
    "block name": {"type": "type name",
                   "color": p_f.pygame.Color,
                   "durability": int},

    "dirt": {"type": "ground",
             "color": p_f.pygame.Color(160, 60, 45, 255),
             "durability": 250},

    "sky": {"type": "air",
            "color": p_f.pygame.Color(125, 125, 250, 150),
            "durability": 0}
}


class Block:
    def __init__(self, pos, size, name, nick, rotation=0, loot=None):
        self.position = pos
        self.size = size
        self.rotation = rotation
        self.name = name
        self.nick = nick
        self.loot = None

        self.color = blocksinfo[self.name]["color"]

        self.body = p_f.pygame.Rect(self.position, self.size)
