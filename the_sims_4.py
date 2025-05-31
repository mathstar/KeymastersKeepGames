from __future__ import annotations

import functools
from enum import Enum
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, Range

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

# Options Dataclass
@dataclass
class TheSims4ArchipelagoOptions:
    pass

# Main Class
class TheSims4Game(Game):
    name = "The Sims 4"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.XONE
    ]

    is_adult_only_or_unrated = False

    options_cls = TheSims4ArchipelagoOptions

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Do a thing",
                data={

                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1
            )
        ]

class Sims4ExpansionPack(Enum):
    GET_TO_WORK = "Get to Work"
    GET_TOGETHER = "Get Together"
    CITY_LIVING = "City Living"
    CATS_AND_DOGS = "Cats & Dogs"
    SEASONS = "Seasons"
    GET_FAMOUS = "Get Famous"
    ISLAND_LIVING = "Island Living"
    DISCOVER_UNIVERSITY = "Discover University"
    ECO_LIFESTYLE = "Eco Lifestyle"
    SNOWY_ESCAPE = "Snowy Escape"
    COTTAGE_LIVING = "Cottage Living"
    HIGH_SCHOOL_YEARS = "High School Years"
    GROWING_TOGETHER = "Growing Together"
    HORSE_RANCH = "Horse Ranch"
    FOR_RENT = "For Rent"
    LOVESTRUCK = "Lovestruck"
    LIFE_AND_DEATH = "Life & Death"
    BUSINESSES_AND_HOBBIES = "Businesses & Hobbies"

class Sims4GamePack(Enum):
    OUTDOOR_RETREAT = "Outdoor Retreat"
    SPA_DAY = "Spa Day"
    DINE_OUT = "Dine Out"
    VAMPIRES = "Vampires"
    PARENTHOOD = "Parenthood"
    JUNGLE_ADVENTURE = "Jungle Adventure"
    STRANGERVILLE = "StrangerVille"
    REALM_OF_MAGIC = "Realm of Magic"
    JOURNEY_TO_BATUU = "Journey to Batuu"
    DREAM_HOME_DECORATOR = "Dream Home Decorator"
    MY_WEDDING_STORIES = "My Wedding Stories"
    WEREWOLVES = "Werewolves"

class Sims4StuffPack(Enum):
    LUXURY_PARTY = "Luxury Party Stuff"
    PERFECT_PATIO = "Perfect Patio Stuff"
    COOL_KITCHEN = "Cool Kitchen Stuff"
    SPOOKY = "Spooky Stuff"
    MOVIE_HANGOUT = "Movie Hangout Stuff"
    ROMANTIC_GARDEN = "Romantic Garden Stuff"
    KIDS_ROOM = "Kids Room Stuff"
    BACKYARD = "Backyard Stuff"
    VINTAGE_GLAMOUR = "Vintage Glamour Stuff"
    BOWLING_NIGHT = "Bowling Night Stuff"
    FITNESS = "Fitness Stuff"
    TODDLER = "Toddler Stuff"
    LAUNDRY_DAY = "Laundry Day Stuff"
    MY_FIRST_PET = "My First Pet Stuff"
    MOSCHINO = "Moschino Stuff"
    TINY_LIVING = "Tiny Living Stuff"
    NIFTY_KNITTING = "Nifty Knitting Stuff"
    PARANORMAL = "Paranormal Stuff"
    HOME_CHEF_HUSTLE = "Home Chef Hustle Stuff"
    CRYSTAL_CREATIONS = "Crystal Creations Stuff"

class Sims4Kit(Enum):
    BUST_THE_DUST = "Bust the Dust Kit"
    COUNTRY_KITCHEN = "Country Kitchen Kit"
    THROWBACK_FIT = "Throwback Fit Kit"
    COURTYARD_OASIS = "Courtyard Oasis Kit"
    INDUSTRIAL_LOFT = "Industrial Loft Kit"
    FASHION_STREET = "Fashion Street Kit"
    INCHEON_ARRIVALS = "Incheon Arrivals Kit"
    BLOOMING_ROOMS = "Blooming Rooms Kit"
    MODERN_MENSWEAR = "Modern Menswear Kit"
    CARNAVAL_STREETWEAR = "Carnaval Streetwear Kit"
    DECOR_TO_THE_MAX = "Decor to the Max Kit"
    MOONLIGHT_CHIC = "Moonlight Chic Kit"
    LITTLE_CAMPERS = "Little Campers Kit"
    FIRST_FITS = "First Fits Kit"
    DESERT_LUXE = "Desert Luxe Kit"
    EVERYDAY_CLUTTER = "Everyday Clutter Kit"
    PASTEL_POP = "Pastel Pop Kit"
    BATHROOM_CLUTTER = "Bathroom Clutter Kit"
    SIMTIMATES_COLLECTION = "Simtimates Collection Kit"
    BASEMENT_TREASURES = "Basement Treasures Kit"
    GREENHOUSE_HAVEN = "Greenhouse Haven Kit"
    GRUNGE_REVIVAL = "Grunge Revival Kit"
    BOOK_NOOK = "Book Nook Kit"
    MODERN_LUXE = "Modern Luxe Kit"
    POOLSIDE_SPLASH = "Poolside Splash Kit"
    CASTLE_ESTATES = "Castle Estates Kit"
    GOTH_GALORE = "Goth Galore Kit"
    URBAN_HOMAGE = "Urban Homage Kit"
    PARTY_ESSENTIALS = "Party Essentials Kit"
    RIVIERA_RETREAT = "Riviera Retreat Kit"
    COZY_BISTRO = "Cozy Bistro Kit"
    ARTIST_STUDIO = "Artist Studio Kit"
    STORYBOOK_NURSERY = "Storybook Nursery Kit"
    CASANOVA_CAVE = "Casanova Cave Kit"
    COMFY_GAMER = "Comfy Gamer Kit"
    SECRET_SANCTUARY = "Secret Sanctuary Kit"
    GOLDEN_YEARS = "Golden Years Kit"
    RESTORATION_WORKSHOP = "Restoration Workshop Kit"

class Sims4CreatorKits(Enum):
    SWEET_SLUMBER_PARTY = "Sweet Slumber Party Creator Kit"
    COZY_KITSCH = "Cozy Kitsch Creator Kit"
    BUSINESS_CHIC = "Business Chic Creator Kit"
    REFINED_LIVING_ROOM = "Refined Living Room Creator Kit"
    SLEEK_BATHROOOM = "Sleek Bathroom Creator Kit"
    SWEET_ALLURE = "Sweet Allure Creator Kit"
