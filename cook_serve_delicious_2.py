from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, Range

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

# Option Dataclass
@dataclass
class CookServeDelicious2ArchipelagoOptions:
    cook_serve_delicious_2_max_yum_level: CookServeDelicious2MaxYumLevel
    cook_serve_delicious_2_display_yum_level_requirements: CookServeDelicious2DisplayYumLevelRequirements

# Main Class
class CookServeDelicious2Game(Game):
    name = "Cook, Serve, Delicious! 2!!"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.SW,
        KeymastersKeepGamePlatforms.XONE
    ]

    is_adult_only_or_unrated = False

    options_cls = CookServeDelicious2ArchipelagoOptions

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Get a Gold medal in SHIFT",
                data={
                    "SHIFT": (self.shifts, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
        ]

    @property
    def max_yum_level(self) -> int:
        return self.archipelago_options.cook_serve_delicious_2_max_yum_level.value

    @property
    def display_yum_level(self) -> int:
        return self.archipelago_options.cook_serve_delicious_2_display_yum_level_requirements.value

    def shifts(self) -> List[str]:
        result = []
        for restaurant, levels in self.chef_for_hire_level_requirements.items():
            for index, level in enumerate(levels):
                if level <= self.max_yum_level:
                    result.append(f"{restaurant} - Shift {index + 1}{ ' (Yum Level ' + str(level) + ')' if self.display_yum_level else ''}")
        return result

    @functools.cached_property
    def chef_for_hire_level_requirements(self) -> Dict[str, List[int]]:
        """A dictionary mapping each Chef for Hire restaurant to the required Yum Level for each shift."""
        return {
            "MAX Wieners": [0, 1, 2, 5, 8, 9, 10, 15],
            "Biggs Burger": [3, 4, 6, 9, 11, 13, 16, 18, 22],
            "Eaty's": [1, 3, 5, 7, 8, 13, 15, 17, 21, 22, 26, 29, 32, 33, 39, 40],
            "Chilly Bowl": [2, 6, 7, 12, 14, 17, 19, 23],
            "Chinese Food": [8, 10, 11, 12, 14, 16, 18, 19, 20, 23, 25, 27, 30, 34],
            "Breakfast & Breakloose": [8, 10, 11, 12, 13, 16, 18, 19, 20, 23, 24, 25, 27, 28, 30, 31],
            "Gree/Itali Casual Dining": [11, 12, 15, 16, 18, 20, 22, 24, 26, 28, 29, 31],
            "Pizza That!": [12, 13, 17, 19, 21, 22, 24, 26, 32],
            "All The Sports Grill": [9, 9, 11, 14, 17, 19, 20, 24, 25, 27, 30, 33, 36, 41],
            "Esteban's": [26, 28, 29, 31, 33, 35, 36, 38, 40, 42, 44, 45, 47, 49, 51],
            "Pie Right": [24, 25, 27, 30, 32, 34, 35, 37, 41, 46],
            "FireKickers": [19, 21, 23, 28, 29, 33, 35, 37, 39, 41, 43, 45, 46, 48],
            "Food Shackers": [20, 25, 26, 29, 31, 32, 34, 36, 38, 40, 42, 44],
            "Slammy's Old Fashioned BBQ": [22, 23, 27, 31, 34, 36, 39, 42, 45, 47, 49, 52, 54, 59],
            "Burrito Time": [16, 18, 22, 28, 35, 40, 46, 49, 50, 52, 53, 57],
            "Contrast Coffee Company": [6, 8, 10, 19, 23, 30, 37, 43, 49, 59, 64, 69, 72, 76],
            "Planet Blue": [34, 38, 47, 61, 63, 65, 73, 77, 78, 84],
            "SubSolutions": [17, 21, 26, 28, 37, 38, 41, 43, 44, 48],
            "The World Tour": [15, 16, 18, 30, 33, 35, 37, 39, 43, 46, 50, 53],
            "Oooh, Organic!": [30, 32, 35, 38, 42, 44, 47, 50],
            "Poppers & Crunchies": [27, 33, 36, 40, 43, 45, 50, 52, 55],
            "The Deep All-You-Can-Eat": [29, 35, 38, 46, 48, 51, 56, 58, 61, 64],
            "The Far East": [31, 37, 38, 45, 49, 53, 57, 60, 62, 67],
            "Good Japan": [32, 37, 40, 43, 48, 51, 55, 59, 63, 65, 70],
            "E": [33, 39, 42, 47, 49, 52, 54, 57, 60, 63, 68, 71, 73, 75, 77, 79],
            "Sushi Nest": [21, 31, 36, 41, 53, 58, 66, 69, 72, 78],
            "Welcome to Tasteville": [46, 50, 56, 61, 64, 69, 72, 74, 76, 80, 82, 84, 86, 89],
            "XLR Purple": [39, 41, 52, 54, 62, 65, 67, 70, 74, 81, 83, 87, 90, 92],
            "Secrets of the Deep": [44, 48, 51, 55, 57, 66, 68, 73, 75, 78, 80, 85, 88, 91],
            "Absolutely": [45, 47, 51, 54, 58, 66, 71, 76, 77, 79, 81, 82],
            "Sebucosto 1991": [48, 55, 56, 59, 62, 65, 68, 74, 80, 83, 86, 93],
            "UEIYAV": [56, 60, 63, 64, 67, 71, 75, 81, 82, 85, 87, 94, 95, 97, 98],
            "Executive's Decision": [70, 73, 79, 80, 84, 88, 89, 91, 92, 93, 95, 96, 97, 98, 99, 100]
        }

    @staticmethod
    def csd_modes() -> List[str]:
        return [
            "Classic",
            "Standard",
            "Stress",
            "Zen"
        ]

    def csd_max_entrees(self):
        """
        Returns the maximum number of entrees that can be served in a single shift.
        This is based on the maximum Yum Level.
        """
        if self.max_yum_level < 4:
            return 3
        elif self.max_yum_level < 14:
            return 4
        elif self.max_yum_level < 18:
            return 5
        else:
            return 6

    def csd_max_sides(self):
        """
        Returns the maximum number of sides that can be served in a single shift.
        This is based on the maximum Yum Level.
        """
        if self.max_yum_level < 7:
            return 1
        elif self.max_yum_level < 21:
            return 2
        else:
            return 3

    def csd_max_drinks(self):
        """
        Returns the maximum number of drinks that can be served in a single shift.
        This is based on the maximum Yum Level.
        """
        if self.max_yum_level < 11:
            return 1
        else:
            return 2

    @functools.cached_property
    def csd_entrees(self) -> List[str]:
        """Entrees that are initially unlocked or can be purchased."""
        return [
            "Chili",
            "Chowder",
            "Gumbo",
            "Soup",
            "Stew",
            "Corndogs",
            "Egg Drop Soup",
            "French Toast",
            "Lasagna",
            "Brisket Slices",
            "Turkey Slices",
            "Ham Slices",
            "Sausage Slices",
            "Muffins",
            "Oatmeal",
            "Pizza by the Slice",
            "Pretzel",
            "Tiramisu",
            "Chicken Sandwich",
            "Japanese Fried Rice",
            "Lamb Chops",
            "Meatloaf",
            "Ribs",
            "Pig's Blood Cake",
            "Tabbouleh",
            "Tamales",
            "Spaghetti",
            "Enchiladas",
            "Rote Grutze",
            "Glazed Donut",
            "Frozen Bananas",
            "Cinnamon Buns",
            "Brownies",
            "Chicken Strips",
            "Fried Shrimp",
            "Steak Fingers",
            "Griddle Eggs",
            "Bean Burger",
            "Chimichanga",
            "Hamburger",
            "Hotdog",
            "Grilled Chicken Sandwich",
            "Sopapillas",
            "Sushi",
            "Turkey Leg",
            "Tres Leches",
            "Breakfast Sandwich",
            "Funnel Cake",
            "Pancakes",
            "Pasta",
            "Lobster",
            "Quesadilla",
            "Ramen",
            "Salisbury Steak",
            "Spinach Veggie Pasta",
            "Steak",
            "Tacos",
            "Traditional Hot Wings",
            "Wok Dish: Beef and Pork",
            "Wok Dish: Chicken",
            "Wok Dish: Shrimp and Veg.",
            "Baked Hot Wings",
            "Calzone",
            "Chicken Breast",
            "Club Sandwich",
            "Corn Chip Pie",
            "Crab Cakes",
            "Crab Legs",
            "Creme Brulee",
            "Dessert Shooters",
            "Fresh Fish",
            "Fried Chicken",
            "Hiyayakko Tofu",
            "Ice Cream Sundae",
            "Japanese Crepe",
            "Steamed Momos",
            "Okonomiyaki",
            "Pizza",
            "Pork Loin",
            "Salad",
            "Samosas",
            "Small Custom Sub",
            "Taiwanese Shaved Ice",
            "Stadium Nachos",
            "Frozen Lattes",
            "Hot Lattes",
            "Iced Lattes",
            "Milkshakes",
            "Smoothies",
            "Espresso Shots",
            "Htapothi sti Skhara",
            "Organic Salad",
            "Ice Cream Scoops",
            "Specialty Donuts",
        ]

    @functools.cached_property
    def csd_locked_entrees(self) -> List[str]:
        """Entrees that are locked and can only be acquired through randomized unlocks."""
        return [
            "Prime Rib",
            "Biscuits and Gravy",
            "Chopped Brisket Sandwich",
            "Roast Beef Sandwich",
            "Slice of Pie",
            "Chow Mein",
            "Deluxe Nachos",
            "Pulled Pork Sandwich",
            "Chicken Nuggets",
            "Fried Fish",
            "Cannoli",
            "Yaki Tomorokoshi",
            "Cereal",
            "Breakfast Burrito",
            "Burrito",
            "Chicken Fried Meats",
            "Filet Mignon",
            "Veal Marsala",
            "Omelette",
            "Sausage and Sauerkraut",
            "Sizzling Fajitas",
            "Sliders",
            "Stuffed Peppers",
            "Tostadas",
            "Waffles",
            "Bananas Foster",
            "Beef Wellington",
            "Carpaccio",
            "Eggplant Parmigiana",
            "Escargot",
            "Gazpacho",
            "Oysters",
            "Pies",
            "Pot Pie",
            "Quiche",
            "Risotto",
            "Sashimi",
            "Shish Kabob",
            "Souffle",
            "Steamed Mussels",
            "Sub Sandwich",
            "Whole Cakes",
            "Yakizakana",
            "Agedashi Tofu",
        ]

    @functools.cached_property
    def csd_sides(self) -> List[str]:
        """Sides that are initially unlocked or can be purchased."""
        return [
            "Asparagus",
            "Bacon",
            "Baked Potato",
            "Black Beans",
            "Broccoli",
            "Brussels Sprouts",
            "Side Chow Mein",
            "Corn on the Cob",
            "Sauerkraut",
            "Dinner Rolls",
            "Edamame",
            "Side Egg Drop Soup",
            "Egg Rolls",
            "Fries",
            "Fried Okra",
            "Fruit Spread",
            "German Red Cabbage",
            "Green Beans",
            "Hash Browns",
            "Japanese Fried Rice Side",
            "Kale Chips",
            "Mac n' Cheese",
            "Mashed Potatoes",
            "Mexican Rice",
            "Onion Rings",
            "Pakora",
            "Peas",
            "Pinto Beans",
            "Potato Salad",
            "Black Rice",
            "Refried Beans",
            "Brown Rice",
            "Sausage Links",
            "Scrambled Eggs",
            "Side Chili",
            "Side Chowder",
            "Side Gumbo",
            "Side Soup",
            "Side Stew",
            "Side Salad",
            "Grits",
            "Steamed Vegetables",
            "Tater Tots",
            "Toast",
            "Tuscan Beans",
            "Cookies",
            "White Rice",
            "Wild Rice",
            "Marshmallow Squares",
            "Croissants",
            "Specialty Fries",
            "Side Oatmeal",
        ]

    @functools.cached_property
    def csd_locked_sides(self) -> List[str]:
        """Sides that are locked and can only be acquired through randomized unlocks."""
        return [
            "Boiled Eggs",
            "Fried Seafood Sides",
            "Grilled Fennel",
            "Kimchi",
            "Onigiri",
            "Roasted Cauliflower",
            "Stuffed Artichokes",
            "Tazukuri",
        ]

    @functools.cached_property
    def csd_drinks(self) -> List[str]:
        """Drinks that are initially unlocked or can be purchased."""
        return [
            "Beer",
            "Coffee",
            "Iced Tea",
            "Juice Bar",
            "Fresh Lemonade",
            "Soda Fountain",
            "Horchata",
            "Hot Tea",
        ]

    @functools.cached_property
    def csd_locked_drinks(self) -> List[str]:
        """Drinks that are locked and can only be acquired through randomized unlocks."""
        return [
            "Craft Beer",
            "Pineapple Juice",
            "Red Wine",
            "White Wine",
        ]

class CookServeDelicious2MaxYumLevel(Range):
    """
    The maximum Yum Level that will be required for trials.

    You should either have a save with at least this Yum Level, or be willing to grind to this Yum Level.
    """
    display_name = "Max Yum Level"
    range_start = 10
    range_end = 125
    default = 50

class CookServeDelicious2DisplayYumLevelRequirements(Toggle):
    """
    Displays the Yum Level requirements for each Chef for Hire shift on the trial description.

    This may be considered spoilers but can be helpful for knowing what level you need to reach for each trial.
    """
    display_name = "Display Yum Level Requirements"
    default = False
