from pythonwarrior.units.base import UnitBase
from pythonwarrior.templates.player import Player
from pythonwarrior.units.golem import Golem
class Warrior(UnitBase):

    def __init__(self):
        super(Warrior, self).__init__()
        self.player_attr = None
        self.name_attr = None
        self.score = 0
        self.golem_abilities = []

    def play_turn(self, turn):
        return self.player().play_turn(turn)

    def player(self):
        if self.player_attr:
            return self.player_attr
        else:
            self.player_attr = Player()
            return self.player_attr

    def earn_points(self, points):
        self.score = self.score + points
        print "earns %d points" % points

    @property
    def attack_power(self):
        return 5

    @property
    def shoot_power(self):
        return 3

    def max_health(self):
        return 20

    def name(self):
        if self.name_attr:
            return self.name_attr
        else:
            return 'Warrior'

    def __repr__(self):
        return self.name()

    @property
    def character(self):
        return "@"

    def perform_turn(self):
        if self.current_turn.action is None:
            self.say('does nothing')
        super(Warrior, self).perform_turn()

    def add_golem_abilities(self, *abilities):
        self.golem_abilities += abilities

    def has_golem(self):
        if self.golem_abilities:
            return True
        else:
            return False

    def base_golem(self):
        golem = Golem()
        golem.add_abilities(*self.golem_abilities)
        return golem
