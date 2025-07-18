# KeymastersKeepGames
My game implementations for [Keymasters Keep](https://github.com/SerpentAI/Archipelago/releases?q=keymaster&expanded=true) -
a custom world for [Archipelago](https://archipelago.gg/) - created by SerpentAI.

# Games
- [[Meta] Archipelago (Categories version)](#meta-archipelago-categories-version)
- [Cook, Serve, Delicious! 2!!](#cook-serve-delicious-2)
- [[Meta] Steam Library](#meta-steam-library)

## [Meta] Archipelago (Categories version)
Archipelago (Categories version) is a meta game that requires you to play Archipelago multiworlds with a specific
number of games from categories you define. The idea is that you have a list of games for each category that will be
chosen from when generating a multiworld. You can choose to have a particular percentage of trials specify that games
must be chosen randomly from each category (randomization must be performed yourself outside of the keep) and a 
percentage of trials that will allow you to choose the games yourself.

### Trial Examples
* Play an Archipelago with 2 FILLER GAMES, 1 MAIN GAMES, and 1 PLAYER'S CHOICE with SELF-CHOSEN games.
* Play an Archipelago with 1 FILLER GAMES, 3 MAIN GAMES, and 1 PLAYER'S CHOICE with RANDOMIZED games.

### Settings
* **archipelago_categories**: A list of the categories you want to use with a minimum and maximum number of games for each.
* **archipelago_categories_randomized_games_chance_percent**: The percentage of trials that will require you to choose games randomly from the categories.
* **archipelago_categories_minimum_games_per_archipelago**: The minimum number of games that will be required for each Archipelago trial.
* **archipelago_categories_maximum_games_per_archipelago**: The maximum number of games that will be required for each Archipelago trial.

```yaml
  archipelago_categories:
    # Specifies the categories to include in each archipelago along with their min and max number of games. You can
    # specify any categories you want.
    FILLER GAMES:
      max_games: 2
      min_games: 0
    MAIN GAMES:
      max_games: 3
      min_games: 1
    PLAYER'S CHOICE:
      max_games: 1
      min_games: 0

  archipelago_categories_randomized_games_chance_percent:
    # The chance that an Archipelago must have its games randomly chosen from each list.
    #
    # You can define additional values between the minimum and maximum values.
    # Minimum value is 0
    # Maximum value is 100
    50: 50
    random: 0
    random-low: 0
    random-high: 0
    never_randomized: 0 # equivalent to 0
    always_randomized: 0 # equivalent to 100

  archipelago_categories_minimum_games_per_archipelago:
    # The minimum number of games that must be included in each Archipelago.
    #
    # You can define additional values between the minimum and maximum values.
    # Minimum value is 1
    # Maximum value is 1000
    1: 50
    random: 0
    random-low: 0
    random-high: 0

  archipelago_categories_maximum_games_per_archipelago:
    # The maximum number of games that can be included in each Archipelago.
    #
    # You can define additional values between the minimum and maximum values.
    # Minimum value is 1
    # Maximum value is 1000
    10: 50
    random: 0
    random-low: 0
    random-high: 0
```

## Cook, Serve, Delicious! 2!!
Cook, Serve, Delicious! 2!! is a fast-paced cooking simulation game where players manage a restaurant and serve various dishes to customers. The game features a variety of food items, cooking mechanics, and challenges.

[Steam](https://store.steampowered.com/app/386620/Cook_Serve_Delicious_2/)

The Keymasters Keep implementation includes trials for all Chef for Hire shifts as well as the Cook, Serve, Delicious 
restaurant for each mode using randomly generated foods.

### Settings

* **include_difficult_objectives (global option):** If difficult objectives are enabled, Stress mode will be included in CSD trails.
* **cook_serve_delicious_2_max_yum_level:** The maximum Yum Level that will be required for trials (Chef for Hire level unlocks, 
and menu slots for CSD). You should either have a save with at least this Yum Level, or be willing to grind to this Yum Level.
* **cook_serve_delicious_2_display_yum_level_requirements:** Displays the Yum Level requirements for each Chef for Hire 
shift on the trial description. Can be helpful for knowing what level you need to reach for each trial, but may be considered spoilers.
* **cook_serve_delicious_2_include_locked_foods:** Include locked entrees, sides, and drinks in the pool for CSD mode trials.
These foods are unlocked randomly when certain milestones are achieved, so it is recommended to only enable this if you 
have a save with all foods unlocked or are willing to grind to unlock them.

```yaml
  cook_serve_delicious_2_max_yum_level:
    # The maximum Yum Level that will be required for trials.
    # 
    # You should either have a save with at least this Yum Level, or be willing to grind to this Yum Level.
    #
    # You can define additional values between the minimum and maximum values.
    # Minimum value is 10
    # Maximum value is 125
    50: 50
    random: 0
    random-low: 0
    random-high: 0

  cook_serve_delicious_2_display_yum_level_requirements:
    # Displays the Yum Level requirements for each Chef for Hire shift on the trial description.
    # 
    # This may be considered spoilers but can be helpful for knowing what level you need to reach for each trial.
    'false': 50
    'true': 0

  cook_serve_delicious_2_include_locked_foods:
    # Include locked entrees, sides, and drinks in the pool for CSD mode trials.
    # 
    # By default, only those foods you start with or can purchase are included, if you enable this option foods that are unlocked
    # randomly at milestones will be included. It is recommended to only enable this if you have a save with all foods unlocked
    # or are willing to grind to unlock them.
    'false': 50
    'true': 0
```

### Credits
- Chef for Hire level requirements sourced from: https://steamcommunity.com/sharedfiles/filedetails/?id=1143264542

## [Meta] Steam Library
Steam Library is a meta game that picks games from your Steam library based on min and max playtime settings. Due to the
nature of using the Steam API this game requires some special handling to set up and generate.

### Setup
* You will need a Steam Web API key to use this game. You can get one from the [Steam API Key page](https://steamcommunity.com/dev/apikey).
* When generating a multiworld with this game, you will need to provide your Steam Web API key as a STEAM_API_KEY environment variable.

### Settings

* **steam_library_min_time_played:** The minimum playtime in minutes for a game to be included in the pool. ("no_limit" is provided as an equivalent to 0)
* **steam_library_max_time_played:** The maximum playtime in minutes for a game to be included in the pool. (use "no_limit" or -1 for no limit, "never_played" is equivalent to 0)
* **steam_library_steam_id:** The Steam ID of the user whose library will be used. You can find your Steam ID by visiting your profile page and looking at the URL, or by using a service like [SteamID.io](https://steamid.io/).
* **steam_library_excluded_games:** A list of game names (must exactly match steam listing including symbols) or Steam App IDs to exclude from the Steam library. This can be used to filter out games you don't want to include in the pool.

```yaml
  steam_library_min_time_played:
    # Only include games from your steam library that have been played at least this many minutes.
    # 
    # Use -1 or "no_limit" for no minimum.
    #
    # You can define additional values between the minimum and maximum values.
    # Minimum value is 0
    # Maximum value is 5256000
    random: 0
    random-low: 0
    random-high: 0
    no_limit: 50 # equivalent to 0

  steam_library_max_time_played:
    # Only include games from your steam library that have been played at most this many minutes.
    # 
    # Use -1 or "no_limit" for no maximum.
    #
    # You can define additional values between the minimum and maximum values.
    # Minimum value is -1
    # Maximum value is 5256000
    random: 0
    random-low: 0
    random-high: 0
    no_limit: 50 # equivalent to -1
    never_played: 0 # equivalent to 0

  steam_library_steam_id:
    # Steam ID to use for fetching the library.
    '': 50

  steam_library_excluded_games:
    # List of game names (must be an exact match) or Steam App IDs to exclude from the Steam library.
    []
```