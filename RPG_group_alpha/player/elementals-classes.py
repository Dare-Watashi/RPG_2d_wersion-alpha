elementals = ['cryo', 'fire', 'hydro', 'nature']


class Basic:
    def __init__(self):
        self.multipliers = {
            'life': 1,
            'health': 1,
            'movement speed': 1,
            'damage': 1,
            'attack speed': 1,
            'critical chance': 1,
            'critical multiplier': 1,
            'healing effectiveness': 1
        }

        self.res = {
            'temperature': 0,
            'cryo': 0,
            'fire': 0,
            'hydro': 0,
            'nature': 0,
            'physical': 0
        }


class Cryo:
    def __init__(self):
        self.multipliers = {
            'life': 1,
            'health': 1,
            'movement speed': 0.9,
            'damage': 1,
            'attack speed': 0.9,
            'critical chance': 1,
            'critical multiplier': 1,
            'healing effectiveness': 1
        }

        self.res = {
            'temperature': 0.05,
            'cryo': 0.1,
            'fire': -0.1,
            'hydro': 0.05,
            'nature': 0,
            'physical': 0.05
        }


class Fire:
    def __init__(self):
        self.multipliers = {
            'life': 0.9,
            'health': 0.9,
            'movement speed': 1,
            'damage': 1.1,
            'attack speed': 1.1,
            'critical chance': 0.9,
            'critical multiplier': 0.9,
            'healing effectiveness': 0.9
        }

        self.res = {
            'temperature': 0.05,
            'cryo': -0.1,
            'fire': 0.1,
            'hydro': -0.05,
            'nature': 0.05,
            'physical': 0
        }


class Hydro:
    def __init__(self):
        self.multipliers = {
            'life': 1.05,
            'health': 1.05,
            'movement speed': 1,
            'damage': 0.9,
            'attack speed': 0.9,
            'critical chance': 1.1,
            'critical multiplier': 1.1,
            'healing effectiveness': 1.05
        }

        self.res = {
            'temperature': -0.05,
            'cryo': 0.05,
            'fire': -0.1,
            'hydro': 0.1,
            'nature': 0.05,
            'physical': 0.05
        }


class Nature:
    def __init__(self):
        self.multipliers = {
            'life': 1.1,
            'health': 1.1,
            'movement speed': 1,
            'damage': 0.9,
            'attack speed': 1,
            'critical chance': 0.9,
            'critical multiplier': 0.9,
            'healing effectiveness': 1.1
        }

        self.res = {
            'temperature': 0,
            'cryo': -0.05,
            'fire': -0.1,
            'hydro': 0.05,
            'nature': 0.1,
            'physical': 0
        }
