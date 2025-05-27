from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

# Option Dataclass
@dataclass
class CookServeDelicious2ArchipelagoOptions:
    pass

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
                label="Do a thing",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
        ]