from otree.api import Currency as c, currency_range
from .pages import *
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):

    def play_round(self):
        yield Instructions,
        if self.player.role() == "Person A":
            yield PersonA, {"allocation": random.randint(0, self.player.endowment)}
        if self.player.role() == "Person B":
            yield PersonB,
        if self.player.role() == "Person C":
            if self.group.treatment != 0:
                yield PersonC1, {"ambiguity_resolved": random.choice([True, False])}
            yield PersonC2, {"punishment": random.randint(0, Constants.max_punishcomp),
                             "compensation": random.randint(0, Constants.max_punishcomp)}
        yield Results
