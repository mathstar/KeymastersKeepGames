from __future__ import annotations

import functools
from os import environ

import requests
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import NamedRange, FreeText

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

# Option Dataclass
@dataclass
class SteamLibraryArchipelagoOptions:
    steam_library_min_time_played: SteamLibraryMinTimePlayed
    steam_library_max_time_played: SteamLibraryMaxTimePlayed
    steam_library_steam_id: SteamLibrarySteamID

# Main Class
class SteamLibraryGame(Game):
    name = "Steam Library"
    platform = KeymastersKeepGamePlatforms.META

    is_adult_only_or_unrated = False

    options_cls = SteamLibraryArchipelagoOptions

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Play GAME from your Steam library",
                data={
                    "GAME": (self.games, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            )
        ]

    def games(self) -> List[str]:
        min_time_played = self.archipelago_options.steam_library_min_time_played.value
        max_time_played = self.archipelago_options.steam_library_max_time_played.value
        print(f"Filtering Steam library games with min_time_played={min_time_played} and max_time_played={max_time_played}")
        return [game["name"] for game in steam_library.games(self.archipelago_options.steam_library_steam_id.value)
                if game["playtime_forever"] >= min_time_played
                and (max_time_played == -1 or game["playtime_forever"] <= max_time_played)]

class SteamLibraryMinTimePlayed(NamedRange):
    """
    Only include games from your steam library that have been played at least this many minutes.
    """
    display_name = "Steam Library Min-Time Played"
    default = "no limit"
    range_start = 0
    range_end = 5256000
    special_range_names = {
        "no limit": 0
    }

class SteamLibraryMaxTimePlayed(NamedRange):
    """
    Only include games from your steam library that have been played at most this many minutes.
    """
    display_name = "Steam Library Max-Time Played"
    default = "no limit"
    range_start = -1
    range_end = 5256000
    special_range_names = {
        "no limit": -1,
        "never played": 0,
    }

class SteamLibrarySteamID(FreeText):
    """
    Steam ID to use for fetching the library.
    """
    display_name = "Steam ID"

class SteamLibraryHolder:
    @functools.lru_cache(maxsize=None)
    def games(self, steam_id) -> List[Dict[str, any]]:
        key = environ.get("STEAM_API_KEY")
        if not key:
            raise RuntimeError("STEAM_API_KEY environment variable is not set")
        print("Fetching games from Steam library...")
        steam_response = requests.get("https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/",
                                      params={
                                          "key": key,
                                          "steamid": steam_id,
                                          "include_appinfo": True,
                                          "include_played_free_games": True,
                                      })
        if steam_response.status_code != 200:
            raise RuntimeError(f"Steam API returned {steam_response.status_code}")
        games_data = steam_response.json().get("response", {}).get("games", [])

        return games_data
steam_library = SteamLibraryHolder()