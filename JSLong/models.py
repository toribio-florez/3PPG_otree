from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from radiogrid import RadioGridField

author = 'Philipp Chapkovski, chapkovski@gmail.com'

doc = """
Justice Sensitivity Inventory:

Schmitt, M., Baumert, A., Gollwitzer, M., & Maes, J. (2010). The Justice Sensitivity Inventory:
Factorial validity, location in the personality facet space, demographic pattern, and normative data.
Social Justice Research, 23(2-3), 211-238.
https://link.springer.com/article/10.1007/s11211-010-0115-2

"""


class Constants(BaseConstants):
    name_in_url = 'Questionnaire'
    players_per_group = None
    num_rounds = 1
    # bigfive = {'Extraversion': [0, 5],
    #            'Agreeableness': [6, 1],
    #            'Conscientiousness': [2, 7],
    #            'Neuroticism': [3, 8],
    #            'Openness': [4, 9]}


class Subsession(BaseSubsession):
   pass

class Group(BaseGroup):
    pass

# Justice Sensitivity Inventory.
# Items
ROWS_JS_V = (
    (1, "It bothers me when others receive something that ought to be mine"),
    (2, "It makes me angry when others receive a reward that I have earned"),
    (3, "I cannot easily bear it when others profit unilaterally from me"),
    (4, "It takes me a long time to forget when I have to fix others’ carelessness"),
    (5, "It gets me down when I get fewer opportunities than others to develop my skills"),
    (6, "It makes me angry when others are undeservingly better off than me"),
    (7, "It worries me when I have to work hard for things that come easily to others"),
    (8, 'I ruminate for a long time when other people are treated better me'),
    (9, 'It burdens me to be criticized for things that are overlooked with others'),
    (10, 'It makes me angry when I am treated worse than others'),
)
ROWS_JS_O = (
    (11, "It bothers me when someone gets something they don’t deserve"),
    (12, "I am upset when someone does not get a reward he/she has earned"),
    (13, "I cannot easily bear it when someone unilaterally profits from others"),
    (14, "It takes me a long time to forget when someone else has to fix others’ carelessness"),
    (15, "It disturbs me when someone receives fewer opportunities to develop his/her skills than others"),
    (16, "I am upset when someone is undeservingly worse off than others"),
    (17, "It worries me when someone has to work hard for things that come easily to others"),
    (18, 'It worries me when someone has to work hard for things that come easily to others'),
    (19, 'It gets me down to see someone criticized for things that are overlooked with others'),
    (20, 'I am upset when someone is treated worse than others'),
)
ROWS_JS_B = (
    (21, "It disturbs me when I receive what others ought to have"),
    (22, "I have a bad conscience when I receive a reward that someone else has earned"),
    (23, "I cannot easily bear it to unilaterally profit from others"),
    (24, "It takes me a long time to forget when others have to fix my carelessness"),
    (25, "It disturbs me when I receive more opportunities than others to develop my skills"),
    (26, "I feel guilty when I am better off than others for no reason"),
    (27, " It bothers me when things come easily to me that others have to work hard for"),
    (28, 'I ruminate for a long time about being treated nicer than others for no reason'),
    (29, 'It bothers me when someone tolerates things with me that other people are being criticized for'),
    (30, 'I feel guilty when I receive better treatment than others'),
)
ROWS_JS_P = (
    (31, "It gets me down when I take something from someone else that I don’t deserve"),
    (32, "I have a bad conscience when I deny someone the acknowledgment he or she deserves"),
    (33, "I cannot stand the feeling of exploiting someone"),
    (34, "It takes me a long time to forget when I allow myself to be careless at the expense of someone else"),
    (35, "It disturbs me when I take away from someone else the possibility of developing his or her potential"),
    (36, "I feel guilty when I enrich myself at the cost of others"),
    (37, "It bothers me when I use tricks to achieve something while others have to struggle for it"),
    (38, 'I ruminate for a long time when I treat someone less friendly than others without a reason'),
    (39, 'I have a bad conscience when I criticize someone for things I tolerate in others'),
    (40, 'I feel guilty when I treat someone worse than others'),
)
# Labels
VALUES = (
    (1, '0'),
    (2, '1'),
    (3, '2'),
    (4, '3'),
    (5, '4'),
    (6, '5')
)

class Player(BasePlayer):
    # Demographics.
    age = models.IntegerField(label='How old are you?',
                              min=18,
                              max=120,
                              blank=True
                              )
    gender = models.IntegerField(
        label="Please select your gender.",
        choices=[
            [1, 'Male'],
            [2, 'Female'],
            [3, 'Other'],
            [4, 'I prefer not to say.'],
        ]
    )
    nstudies = models.IntegerField(
        label="Please estimate how many MTurk studies you have participated in (excluding this study)",
        choices=[
            [1, 'Less than 5 studies'],
            [2, 'Between 5 and less than 10 studies.'],
            [3, 'between 10 and less than 15 studies.'],
            [4, '15 or more studies.'],
            [5, 'I prefer not to say.']
        ]
    )
    degree = models.IntegerField(
        label="Please indicate the highest academic degree you have completed. If you are currently actively pursuing one, please select that academic degree.",
        choices=[
            [1, 'High school or lower'],
            [2, 'Bachelor degree'],
            [3, 'Master degree'],
            [4, 'PhD degree'],
            [5, 'MBA degree'],
            [6, 'Other'],
            [7, 'I prefer not to say.']
        ]
    )


    JS_V = RadioGridField(rows=ROWS_JS_V, values=VALUES, require_all_fields=True,
                          verbose_name="", null=True)
    JS_O = RadioGridField(rows=ROWS_JS_O, values=VALUES, require_all_fields=True,
                          verbose_name="", null=True)
    JS_B = RadioGridField(rows=ROWS_JS_B, values=VALUES, require_all_fields=True,
                          verbose_name="", null=True)
    JS_P = RadioGridField(rows=ROWS_JS_P, values=VALUES, require_all_fields=True,
                          verbose_name="", null=True)