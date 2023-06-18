from services import Services
from character import Character

class Query:
    def __init__(self) -> None:
        self.services = Services()
        self.character = Character("bob", "forest", 14, "important_area1", "hunting", "", "")
        self.is_area_valid = self.services.is_Area_Valid(self.character.important_area)
        self.is_Success = self.services.rand_Num_Generator() > 29
        self.general_bonus = self.character.general_bonus
        self.is_general_bonus = self.character.specific_bonus == "foran gevir"
        self.num_of_items = self.services.rand_Num_Generator
query = Query()

area = query.is_area_valid
print(area)