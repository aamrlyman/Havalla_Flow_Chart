import random 

class Services:
    def __init__(self) -> None:        
        pass
    def is_Area_Valid(self, important_area: str) -> bool:
            return important_area.count(important_area) > 0
    def rand_Num_Generator(self, list=[{"":int}]):
        range_max = 100
        if(len(list) > 0):
            final_item = list[len(list) -1]
            for key in final_item:
                range_max = final_item[key]
                return random.randrange(1, range_max)             
        return random.randrange(1,range_max)
    
    # def get_object_range(self, obj:{}) -> int: #type: ignore
    #      stack = []


