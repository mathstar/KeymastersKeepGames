# KeymastersKeepGames
My game implementations for [Keymasters Keep](https://github.com/SerpentAI/Archipelago/releases?q=keymaster&expanded=true) -
a custom world for [Archipelago](https://archipelago.gg/) - created by SerpentAI.

# Games
- [Cook, Serve, Delicious! 2!!](#cook-serve-delicious-2)

## Cook, Serve, Delicious! 2!!
Cook, Serve, Delicious! 2!! is a fast-paced cooking simulation game where players manage a restaurant and serve various dishes to customers. The game features a variety of food items, cooking mechanics, and challenges.

[Steam](https://store.steampowered.com/app/386620/Cook_Serve_Delicious_2/)

### Settings

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