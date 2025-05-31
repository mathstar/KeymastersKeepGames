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

class Sims4Skill:
    name: str
    max_level: int
    required_packs: Set[Sims4ExpansionPack | Sims4GamePack | Sims4StuffPack | Sims4Kit | Sims4CreatorKits]
    age: str

    def __init__(self, name: str, max_level: int,
                 required_packs: Set[Sims4ExpansionPack | Sims4GamePack | Sims4StuffPack | Sims4Kit | Sims4CreatorKits] = None,
                 age: str = "Adult"):
        self.name = name
        self.max_level = max_level
        if required_packs is None:
            required_packs = set()
        self.required_packs = required_packs
        self.age = age

sims4_skills = [
    # Base Game Skills
    Sims4Skill(
        name="Charisma",
        max_level=10,
    ),
    Sims4Skill(
        name="Comedy",
        max_level=10,
    ),
    Sims4Skill(
        name="Cooking",
        max_level=10,
    ),
    Sims4Skill(
        name="Fishing",
        max_level=10,
    ),
    Sims4Skill(
        name="Fitness",
        max_level=10,
    ),
    Sims4Skill(
        name="Gardening",
        max_level=10,
    ),
    Sims4Skill(
        name="Gourmet Cooking",
        max_level=10,
    ),
    Sims4Skill(
        name="Guitar",
        max_level=10,
    ),
    Sims4Skill(
        name="Handiness",
        max_level=10,
    ),
    Sims4Skill(
        name="Logic",
        max_level=10,
    ),
    Sims4Skill(
        name="Mischief",
        max_level=10,
    ),
    Sims4Skill(
        name="Mixology",
        max_level=10,
    ),
    Sims4Skill(
        name="Painting",
        max_level=10,
    ),
    Sims4Skill(
        name="Photography",
        max_level=5,
    ),
    Sims4Skill(
        name="Piano",
        max_level=10,
    ),
    Sims4Skill(
        name="Programming",
        max_level=10,
    ),
    Sims4Skill(
        name="Rocket Science",
        max_level=10,
    ),
    Sims4Skill(
        name="Video Gaming",
        max_level=10,
    ),
    Sims4Skill(
        name="Violin",
        max_level=10,
    ),
    Sims4Skill(
        name="Writing",
        max_level=10,
    ),

    # Toddler Skills
    Sims4Skill(
        name="Communication",
        max_level=5,
        age="Toddler"
    ),
    Sims4Skill(
        name="Imagination",
        max_level=5,
        age="Toddler"
    ),
    Sims4Skill(
        name="Movement",
        max_level=5,
        age="Toddler"
    ),
    Sims4Skill(
        name="Potty",
        max_level=5,
        age="Toddler"
    ),
    Sims4Skill(
        name="Thinking",
        max_level=5,
        age="Toddler"
    ),

    # Child Skills
    Sims4Skill(
        name="Creativity",
        max_level=10,
        age="Child"
    ),
    Sims4Skill(
        name="Mental",
        max_level=10,
        age="Child"
    ),
    Sims4Skill(
        name="Motor",
        max_level=10,
        age="Child"
    ),
    Sims4Skill(
        name="Social",
        max_level=10,
        age="Child"
    ),

    # Outdoor Retreat Skills
    Sims4Skill(
        name="Herbalism",
        max_level=10,
        required_packs={Sims4GamePack.OUTDOOR_RETREAT}
    ),

    # Get to Work Skills
    Sims4Skill(
        name="Baking",
        max_level=10,
        required_packs={Sims4ExpansionPack.GET_TO_WORK}
    ),

    # Spa Day Skills
    Sims4Skill(
        name="Wellness",
        max_level=10,
        required_packs={Sims4GamePack.SPA_DAY}
    ),

    # Get Together Skills
    Sims4Skill(
        name="Dancing",
        max_level=5,
        required_packs={Sims4ExpansionPack.GET_TOGETHER}
    ),
    Sims4Skill(
        name="DJ Mixing",
        max_level=10,
        required_packs={Sims4ExpansionPack.GET_TOGETHER}
    ),

    # City Living Skills
    Sims4Skill(
        name="Singing",
        max_level=10,
        required_packs={Sims4ExpansionPack.CITY_LIVING}
    ),

    # Vampires Skills
    Sims4Skill(
        name="Pipe Organ",
        max_level=10,
        required_packs={Sims4GamePack.VAMPIRES}
    ),
    Sims4Skill(
        name="Vampire Lore",
        max_level=15,
        required_packs={Sims4GamePack.VAMPIRES}
    ),

    # Bowling Night Skills
    Sims4Skill(
        name="Bowling",
        max_level=5,
        required_packs={Sims4StuffPack.BOWLING_NIGHT}
    ),

    # Parenthood Skills
    Sims4Skill(
        name="Parenting",
        max_level=10,
        required_packs={Sims4GamePack.PARENTHOOD}
    ),

    # Cats & Dogs Skills
    Sims4Skill(
        name="Pet Training",
        max_level=5,
        required_packs={Sims4ExpansionPack.CATS_AND_DOGS}
    ),
    Sims4Skill(
        name="Veterinarian",
        max_level=10,
        required_packs={Sims4ExpansionPack.CATS_AND_DOGS}
    ),

    # Jungle Adventure Skills
    Sims4Skill(
        name="Archaeology",
        max_level=10,
        required_packs={Sims4GamePack.JUNGLE_ADVENTURE}
    ),
    Sims4Skill(
        name="Selvadoradian Culture",
        max_level=10,
        required_packs={Sims4GamePack.JUNGLE_ADVENTURE}
    ),

    # Seasons Skills
    Sims4Skill(
        name="Flower Arranging",
        max_level=10,
        required_packs={Sims4ExpansionPack.SEASONS}
    ),

    # Get Famous Skills
    Sims4Skill(
        name="Acting",
        max_level=10,
        required_packs={Sims4ExpansionPack.GET_FAMOUS}
    ),
    Sims4Skill(
        name="Media Production",
        max_level=5,
        required_packs={Sims4ExpansionPack.GET_FAMOUS}
    ),

    # Discover University Skills
    Sims4Skill(
        name="Research & Debate",
        max_level=10,
        required_packs={Sims4ExpansionPack.DISCOVER_UNIVERSITY}
    ),
    Sims4Skill(
        name="Robotics",
        max_level=10,
        required_packs={Sims4ExpansionPack.DISCOVER_UNIVERSITY}
    ),

    # Eco Lifestyle Skills
    Sims4Skill(
        name="Fabrication",
        max_level=10,
        required_packs={Sims4ExpansionPack.ECO_LIFESTYLE}
    ),
    Sims4Skill(
        name="Juice Fizzing",
        max_level=5,
        required_packs={Sims4ExpansionPack.ECO_LIFESTYLE}
    ),

    # Nifty Knitting Skills
    Sims4Skill(
        name="Knitting",
        max_level=10,
        required_packs={Sims4StuffPack.NIFTY_KNITTING}
    ),

    # Snowy Escape Skills
    Sims4Skill(
        name="Rock Climbing",
        max_level=10,
        required_packs={Sims4ExpansionPack.SNOWY_ESCAPE}
    ),
    Sims4Skill(
        name="Skiing",
        max_level=10,
        required_packs={Sims4ExpansionPack.SNOWY_ESCAPE}
    ),
    Sims4Skill(
        name="Snowboarding",
        max_level=10,
        required_packs={Sims4ExpansionPack.SNOWY_ESCAPE}
    ),

    # Paranormal Skills
    Sims4Skill(
        name="Medium",
        max_level=5,
        required_packs={Sims4StuffPack.PARANORMAL}
    ),

    # Cottage Living Skills
    Sims4Skill(
        name="Cross-Stitch",
        max_level=5,
        required_packs={Sims4ExpansionPack.COTTAGE_LIVING}
    ),

    # High School Years Skills
    Sims4Skill(
        name="Entrepreneur",
        max_level=5,
        required_packs={Sims4ExpansionPack.HIGH_SCHOOL_YEARS}
    ),

    # Horse Ranch Skills
    Sims4Skill(
        name="Horse Riding",
        max_level=10,
        required_packs={Sims4ExpansionPack.HORSE_RANCH}
    ),
    Sims4Skill(
        name="Nectar Making",
        max_level=5,
        required_packs={Sims4ExpansionPack.HORSE_RANCH}
    ),
    Sims4Skill(
        name="Agility (Horse)",
        max_level=10,
        required_packs={Sims4ExpansionPack.HORSE_RANCH},
        age="Horse"
    ),
    Sims4Skill(
        name="Endurance (Horse)",
        max_level=10,
        required_packs={Sims4ExpansionPack.HORSE_RANCH},
        age="Horse"
    ),
    Sims4Skill(
        name="Jumping (Horse)",
        max_level=10,
        required_packs={Sims4ExpansionPack.HORSE_RANCH},
        age="Horse"
    ),
    Sims4Skill(
        name="Temperament (Horse)",
        max_level=10,
        required_packs={Sims4ExpansionPack.HORSE_RANCH},
        age="Horse"
    ),

    # Crystal Creations Skills
    Sims4Skill(
        name="Gemology",
        max_level=10,
        required_packs={Sims4StuffPack.CRYSTAL_CREATIONS}
    ),

    # Lovestruck Skills
    Sims4Skill(
        name="Romance",
        max_level=10,
        required_packs={Sims4ExpansionPack.LOVESTRUCK}
    ),

    # Life & Death Skills
    Sims4Skill(
        name="Thanatology",
        max_level=5,
        required_packs={Sims4ExpansionPack.LIFE_AND_DEATH}
    ),

    # Businesses & Hobbies Skills
    Sims4Skill(
        name="Pottery",
        max_level=10,
        required_packs={Sims4ExpansionPack.BUSINESSES_AND_HOBBIES}
    ),
    Sims4Skill(
        name="Tattooing",
        max_level=10,
        required_packs={Sims4ExpansionPack.BUSINESSES_AND_HOBBIES}
    ),
]
