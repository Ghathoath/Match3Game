import pygame
from enum import Enum

def swap(value1,value2):
    value1,value2=value2,value1

class test(Enum):
    EMPTY = 0
    PHYSICAL_ATTACK = 1
    MAGIC_ATTACK = 2
    HP_POTION = 3
    MP_POTION = 4

print(type(test.HP_POTION))

