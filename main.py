from data import *
from character import Character
from services import Services

bob = Character("bob", "forest", 12,"important_area1", "exploring", "foreign_gravear" )
services = Services()

is_valid = services.is_Area_Valid(bob.important_area)
print(is_valid)

isSuccess = services.rand_Num_Generator([])
print(isSuccess)

