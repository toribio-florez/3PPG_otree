from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class JS_V(Page):
    form_model = 'player'
    form_fields = ['JS_V']

class JS_O(Page):
    form_model = 'player'
    form_fields = ['JS_O']

class JS_B(Page):
    form_model = 'player'
    form_fields = ['JS_B']

class JS_P(Page):
    form_model = 'player'
    form_fields = ['JS_P']

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'nstudies','degree']


page_sequence = [
    JS_V,
    JS_O,
    JS_B,
    JS_P,
    Demographics
]
