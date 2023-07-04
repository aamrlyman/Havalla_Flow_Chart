important_areas = ["important_area1", "important_area2", "important_area1", ]

activity_specific_bonuses = {
    "screech_owl": {
        "effect": "retry on failed role",
        "is_retry": True
    }
}

is_successful_activity = {
    "failure": 30,
    "success": 100,
}

num_of_items_base = {
    1: 13,
    2: 63,
    3: 89,
    4: 100
}

num_of_items_FG = {
    1: 10,
    2: 60,
    3: 85,
    4: 100
}

item_quality_Exploration = {
    "poor": {
        "range": 40,
        "categories":
        {
            "vendor trash": {"range": 15,
                             "items":
                             [
                                 {
                                     "name": "cool stick",
                                     "id": 1,
                                     "link": "www.coolpic/1.com"
                                 },
                                 {
                                     "name": "rabbit foot",
                                     "id": 2,
                                     "link": "www.coolpic/2.com"
                                 },
                             ]
                             },
            "crafted": 30,
            "ore": 45,
            "meat": 60,
            "bone": 75,
            "pelt": 90,
            "herb": 105,
        }
    },
    "common": {
        "range": 70,
        "categories":
        {
            "vendor trash": 6,
            "consumables": 12,
            "crafted": 19,
            "tools": 26,
            "ore": 33,
            "gem": 40,
            "meat": 47,
            "bone": 54,
            "pelt": 61,
            "vegetable": 68,
            "fruit": 75,
            "herb": 82,
            "plant": 89,
            "accessories/armor/cosmetic": 96,
            "companion": 100,
        }
    },
    "uncommon": {
        "range": 70,
        "categories":
        {
            "vendor trash": 8,
            "consumables": 16,
            "crafted": 24,
            "ore": 32,
            "gem": 40,
            "meat": 48,
            "bone": 56,
            "pelt": 64,
            "fruit": 72,
            "plant": 81,
            "accessories/armor/cosmetic": 90,
            "companion": 100,
        }
    },
    "rare": {
        "range": 97,
        "categories":
        {
            "vendor trash": 11,
            "crafted": 22,
            "ore": 33,
            "gem": 44,
            "meat": 55,
            "bone": 66,
            "pelt": 77,
            "fruit": 88,
            "accessories/armor/cosmetic": 99,
        }
    },
    "epic": {
        "range": 100,
        "categories":
        {
            "vendor trash": 14,
            "consumable": 28,
            "crafted": 42,
            "tools": 56,
            "ore": 70,
            "gem": 84,
            "herb": 98,
        }
    }
}

item_quality_hunting = {
    "poor/common": 70,
    "uncommon": 95,
    "rare": 100
}

is_injured = {
    "injured": 30,
    "unharmed": 100,
}

vendor_trash = [
    {"name": "ice cream",
     "link": "www.link.com",
     "id": 454,
     },
    {"name": "ice cream",
     "link": "www.link.com",
     "id": 454,
     },
]

injuries = {
    "sprain": {"range": 20, "impact": "-5 hp,  -1 sp agility"},
    "defeaned": {"range": 30, "impact": "-5 hp,  -1 sp agility"},
    "concussion": {"range": 40, "impact": "-25 hp, -3 sp intellect"},
    "fracture": {"range": 50, "impact": "-10 hp, -2 sp strength"},
    "minor open wound": {"range": 60, "impact": "-10 hp, -2 sp stamina"},
    "curse": {"range": 68, "impact": "-1 sp all stats"},
    "poison": {"range": 75, "impact": "-30 hp -2 sp stamina && -2 agility"},
    "internal injury": {"range": 84, "impact": "-25 hp -3 sp stamina"},
    "broken bone": {"range": 89, "impact": "-50 hp -4 sp strength"},
    "sever open wound": {"range": 94, "impact": "-50 hp -4 sp stamina"},
    "unstoppable bleed": {"range": 100, "impact": "-50 hp -4 sp stamina && -4 stength"},
}
