from character import Character
from services import Services
from data import *

class Run: 
    def __init__(self):
        self.character = Character("bob", "forest", 12,"important_area1", "exploring", "foreign_gravear" )
        self.services = Services()
        def execute():
            bob = self.character
            services = self.services
            if(not services.is_Area_Valid(bob.important_area)):
                return "That is not a valid area"
            if(services.rand_Num_Generator() < 31 and not bob.specific_bonus):
                return "It was an unsuccessful expedition"
            elif(bob.specific_bonus and (services.rand_Num_Generator() < 31)):
                    return "It was an unsuccessful expedition"
            num_of_items_role = services.rand_Num_Generator()
            num_of_items_obj = num_of_items_FG if bob.general_bonus else num_of_items_base 
            
            for key in (num_of_items_obj):
                 obj_num = num_of_items_obj[key]
                 difference = obj_num - num_of_items_role
                 if(difference > -1  and difference < obj_num):
                    num_of_items = key

            for int in num_of_items: # type: ignore
                item_qualities = []
                item_qualities.append(services.rand_Num_Generator())

            for num in item_qualities: #type: ignore
                items = []
                item = {"quality": "", "category": "", "name":"", "id": 0, "link": ""}
                


            
                 


