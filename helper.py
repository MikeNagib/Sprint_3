from random import randint
from data import *


def generate_login():
    return EMAIL_USER + COGORTA_ID + str(randint(000, 999)) + "@" + EMAIL_DOMAIN


def generate_password():
    password = randint(1000001, 9999999)
    return password
