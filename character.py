class Character:
    def __init__(self, name: str, zone: str, character_id: int, important_area: str, activity: str, specific_bonus= "", general_bonus="") -> None:
        self.name = name
        self.character_id = character_id
        self.zone = zone
        self.important_area = important_area
        self.activity = activity
        self.general_bonus = general_bonus
        self.specific_bonus = specific_bonus
