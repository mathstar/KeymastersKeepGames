from __future__ import annotations

import itertools
from typing import List

from dataclasses import dataclass

from Options import NamedRange, OptionDict, Range
from schema import Schema

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


# Option Dataclass
@dataclass
class ArchipelagoCategoriesArchipelagoOptions:
    archipelago_categories: ArchipelagoCategories
    archipelago_categories_randomized_games_chance_percent: RandomizedGamesChancePercent
    archipelago_categories_minimum_games_per_archipelago: MinimumGamesPerArchipelago
    archipelago_categories_maximum_games_per_archipelago: MaximumGamesPerArchipelago

# Main Class
class ArchipelagoCategoriesGame(Game):
    name = "Archipelago (Categories version)"
    platform = KeymastersKeepGamePlatforms.META

    is_adult_only_or_unrated = False

    options_cls = ArchipelagoCategoriesArchipelagoOptions

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        archipelago_categories = self.archipelago_options.archipelago_categories.value
        randomized_games_chance_percent = self.archipelago_options.archipelago_categories_randomized_games_chance_percent.value
        minimum_games_per_archipelago = self.archipelago_options.archipelago_categories_minimum_games_per_archipelago.value
        maximum_games_per_archipelago = self.archipelago_options.archipelago_categories_maximum_games_per_archipelago.value

        objective_templates = []

        # Generate all possible combinations of games per category within min-max constraints
        category_names = list(archipelago_categories.keys())
        category_ranges = []

        # Create ranges for each category based on min and max games
        for category in category_names:
            min_games = archipelago_categories[category]["min_games"]
            max_games = archipelago_categories[category]["max_games"]
            category_ranges.append(range(min_games, max_games + 1))

        # Generate all possible combinations
        for combo in itertools.product(*category_ranges):
            # Check if total is within global min-max range
            total_games = sum(combo)
            if minimum_games_per_archipelago <= total_games <= maximum_games_per_archipelago:
                # Create a human-readable label for this combination
                label_parts = []
                category_counts = {}

                for i, count in enumerate(combo):
                    category = category_names[i]
                    if count > 0:
                        category_counts[category] = count
                        label_parts.append(f"{count} {category}")

                if len(label_parts) > 1:
                    label = "Play an Archipelago with " + ", ".join(label_parts[:-1]) + ", and " + label_parts[-1]
                else:
                    label = "Play an Archipelago with " + label_parts[0]

                # Create the GameObjectiveTemplate
                objective_templates.append(GameObjectiveTemplate(
                    label=label + " with RANDOMIZED games.",
                    data={},
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=randomized_games_chance_percent,
                ))
                objective_templates.append(GameObjectiveTemplate(
                    label=label + " with SELF-CHOSEN games.",
                    data={},
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=100 - randomized_games_chance_percent,
                ))

        return objective_templates

# Archipelago Options
class ArchipelagoCategories(OptionDict):
    """
    Specifies the categories to include in each archipelago along with their min and max number of games. You can
    specify any categories you want.
    """

    display_name = "Archipelago Categories"
    default = {
        "MAIN GAMES": {
            "min_games": 1,
            "max_games": 3
        },
        "FILLER GAMES": {
            "min_games": 0,
            "max_games": 2
        },
        "PLAYER'S CHOICE": {
            "min_games": 0,
            "max_games": 1
        },
    }
    schema = Schema(
        {
            str: {
                "min_games": int,
                "max_games": int
            }
        }
    )

class RandomizedGamesChancePercent(NamedRange):
    """
    The chance that an Archipelago must have its games randomly chosen from each list.
    """
    display_name = "Randomized Games Chance Percent"
    default = 50
    range_start = 0
    range_end = 100
    special_range_names = {
        "never_randomized": 0,
        "always_randomized": 100
    }

class MinimumGamesPerArchipelago(Range):
    """
    The minimum number of games that must be included in each Archipelago.
    """
    display_name = "Minimum Games Per Archipelago"
    default = 1
    range_start = 1
    range_end = 1000

class MaximumGamesPerArchipelago(Range):
    """
    The maximum number of games that can be included in each Archipelago.
    """
    display_name = "Maximum Games Per Archipelago"
    default = 10
    range_start = 1
    range_end = 1000
