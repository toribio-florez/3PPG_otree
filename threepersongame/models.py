from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, Currency as c,
)
import itertools
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'threepersongame'
    players_per_group = 3
    num_rounds = 1
    max_punishcomp = c(10)  # Maximum third-party can Punish or Compensate.
    endow_B = c(0)
    endow_C = c(10)


class Subsession(BaseSubsession):
    # Uses the Group variable "treatment" for iterating between the different Treatments and define the Endowment of Person A.
    def creating_session(self):
        pass

class Group(BaseGroup):
    treatment = models.IntegerField(choices=[
        [0, 'No Ambiguity'],
        [1, 'Ambiguity'],
        [2, 'Ambiguity_Solve'],
    ])
    endow_A = models.CurrencyField()
    payoff = models.CurrencyField()
    # Every decision is defined at the Group level, because they belong to individual roles.

    # Dynamically define the maximum allocation as the "Endowment of A".
    allocation = models.CurrencyField(min=0,
                                      label='How much would you like to send to Person B?')

    def allocation_max(self):
        return self.endow_A

        # Punishment and Compensation.

    punishment = models.CurrencyField(min=0,
                                      max=Constants.max_punishcomp,
                                      label='Do you want to deduct any amount from Person A?')
    compensation = models.CurrencyField(min=0,
                                        max=Constants.max_punishcomp,
                                        label='Do you want to send any amount from Person B?')

    ambiguity_resolved = models.BooleanField(widget=widgets.CheckboxInput,blank=True)
    # If we want to make the decision a YES or NO.
    # ambiguity_resolved = models.BooleanField(widget=widgets.RadioSelectHorizontal)

    def set_endowment(self):
        personA = self.get_player_by_role("Person A")
        personB = self.get_player_by_role("Person B")
        personC = self.get_player_by_role("Person C")
        personA.endowment = self.endow_A
        personB.endowment = Constants.endow_B
        personC.endowment = Constants.endow_C

    def set_payoffs(self):
        personA = self.get_player_by_role("Person A")
        personB = self.get_player_by_role("Person B")
        personC = self.get_player_by_role("Person C")
        personA.payoff = personA.endowment - self.allocation - self.punishment
        personB.payoff = personB.endowment + self.allocation + self.compensation
        personC.payoff = personC.endowment - 0.5 * self.punishment - 0.5 * self.compensation


class Player(BasePlayer):

    def role(self):
        roles = {1: "Person A", 2: "Person B", 3: "Person C"}
        return roles.get(self.id_in_group, "")


    endowment = models.CurrencyField()


# Define endowments for each Role.


# Define payoffs for each Role.
