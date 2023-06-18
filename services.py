import random 

class Services:
    def __init__(self) -> None:
        self.important_areas = ["important_area1","important_area2","important_area1", ]
        self.general_bonuses = [{"name": "foran_gavir", 15: "one item"}]
        self.specific_bonuses = [{"name": "screech_owl", "ability": "cool stuff"}]
    def is_Area_Valid(self, important_area: str) -> bool:
            return self.important_areas.count(important_area) > 0
    def rand_Num_Generator(self, list=[{"":int}]):
        range_max = 100
        if(len(list) > 0):
            final_item = list[len(list) -1]
            for key in final_item:
                range_max = final_item[key]
                return random.randrange(1, range_max)             
        return random.randrange(1,range_max)

