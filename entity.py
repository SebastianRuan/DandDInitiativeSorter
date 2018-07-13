import functools


# @functools.total_ordering
class Entity:
    def __init__(self, name, hp, initiative):
        self.name = name
        self.hp = hp
        self.initiative = initiative

    def __lt__(self, other):
        return self.initiative < other.initiative

    def __eq__(self, other):
        return self.initiative == other

    def __repr__(self):
        return "Entity('{}', '{}', {},)".format(self.name, self.hp, self.initiative)

    def __str__(self):
        return "{} - {}".format(self.name, self.hp)

class Player(Entity):
    def __init__(self, name, hp, initiative):
        super().__init__(name, hp, initiative)
        self.death_throws = 0

    def increment_dt(self):
        self.death_throws += 1

class Enemy(Entity):
    def take_damage(self, damage):
        self.hp -= damage
