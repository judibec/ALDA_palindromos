import random
import string
from execution import constants


def getRandomStrings(sizeString=constants.LIMIT):
    return ''.join(random.choices(string.ascii_lowercase, k=sizeString))
