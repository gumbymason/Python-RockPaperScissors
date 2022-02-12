import random
choices = ['Rock', 'Paper', 'Scissors']







__version__ = '0.1'
__author__ = 'Mason Grant'

# create the Model for the app
class Choice:
    def CPUChoice():
        """make CPU's choice"""
        pick = random.choice(choices)
        return pick