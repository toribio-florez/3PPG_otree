from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class MatchingWP(WaitPage):
    group_by_arrival_time = True

    def is_displayed(self) -> bool:
        return self.round_number == 1

    def after_all_players_arrive(self):
        g = self.group
        corrected_group_id = g.id_in_subsession - 1
        g.treatment = corrected_group_id % 3
        if g.treatment == 0:
            g.endow_A = c(10)
        else:
            g.endow_A = c(random.randint(2, 10))

        players = self.group.get_players()
        random.shuffle(players)
        self.group.set_players(players)
        self.group.set_endowment()


class Instructions(Page):
    pass


class PersonA(Page):
    form_model = 'group'
    form_fields = ['allocation']

    def is_displayed(self):
        return self.player.role() == "Person A"


class WaitA(WaitPage):
    pass


class PersonB(Page):
    def is_displayed(self):
        return self.player.role() == "Person B"


class PersonC1(Page):
    form_model = 'group'
    form_fields = ['ambiguity_resolved']

    def is_displayed(self):
        return self.player.role() == "Person C" and self.group.treatment != 0


class PersonC2(Page):
    form_model = 'group'
    form_fields = ['punishment', 'compensation']

    def is_displayed(self):
        return self.player.role() == "Person C"


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    pass


page_sequence = [
    MatchingWP,
    Instructions,
    PersonA,
    WaitA,
    PersonB,
    PersonC1,
    PersonC2,
    ResultsWaitPage,
    Results,
]
