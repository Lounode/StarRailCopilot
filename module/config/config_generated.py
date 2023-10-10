import datetime

# This file was automatically generated by module/config/config_updater.py.
# Don't modify it manually.


class GeneratedConfig:
    """
    Auto generated configuration
    """

    # Group `Scheduler`
    Scheduler_Enable = False  # True, False
    Scheduler_NextRun = datetime.datetime(2020, 1, 1, 0, 0)
    Scheduler_Command = 'Alas'
    Scheduler_ServerUpdate = '04:00'

    # Group `Emulator`
    Emulator_Serial = 'auto'
    Emulator_PackageName = 'auto'  # auto, CN-Official, CN-Bilibili, OVERSEA-America, OVERSEA-Asia, OVERSEA-Europe, OVERSEA-TWHKMO
    Emulator_GameLanguage = 'auto'  # auto, cn, en
    Emulator_ScreenshotMethod = 'auto'  # auto, ADB, ADB_nc, uiautomator2, aScreenCap, aScreenCap_nc, DroidCast, DroidCast_raw, scrcpy
    Emulator_ControlMethod = 'MaaTouch'  # minitouch, MaaTouch
    Emulator_AdbRestart = False

    # Group `EmulatorInfo`
    EmulatorInfo_Emulator = 'auto'  # auto, NoxPlayer, NoxPlayer64, BlueStacks4, BlueStacks5, BlueStacks4HyperV, BlueStacks5HyperV, LDPlayer3, LDPlayer4, LDPlayer9, MuMuPlayer, MuMuPlayerX, MuMuPlayer12, MEmuPlayer
    EmulatorInfo_name = None
    EmulatorInfo_path = None

    # Group `Error`
    Error_Restart = 'game'  # game, game_emulator
    Error_SaveError = True
    Error_ScreenshotLength = 1
    Error_OnePushConfig = 'provider: null'

    # Group `Optimization`
    Optimization_ScreenshotInterval = 0.3
    Optimization_CombatScreenshotInterval = 1.0
    Optimization_WhenTaskQueueEmpty = 'goto_main'  # stay_there, goto_main, close_game

    # Group `Dungeon`
    Dungeon_Name = 'Calyx_Golden_Treasures'  # Calyx_Golden_Memories, Calyx_Golden_Aether, Calyx_Golden_Treasures, Calyx_Crimson_Destruction, Calyx_Crimson_Preservation, Calyx_Crimson_The_Hunt, Calyx_Crimson_Abundance, Calyx_Crimson_Erudition, Calyx_Crimson_Harmony, Calyx_Crimson_Nihility, Stagnant_Shadow_Quanta, Stagnant_Shadow_Gust, Stagnant_Shadow_Fulmination, Stagnant_Shadow_Blaze, Stagnant_Shadow_Spike, Stagnant_Shadow_Rime, Stagnant_Shadow_Mirage, Stagnant_Shadow_Icicle, Stagnant_Shadow_Doom, Stagnant_Shadow_Puppetry, Stagnant_Shadow_Abomination, Stagnant_Shadow_Celestial, Cavern_of_Corrosion_Path_of_Gelid_Wind, Cavern_of_Corrosion_Path_of_Jabbing_Punch, Cavern_of_Corrosion_Path_of_Drifting, Cavern_of_Corrosion_Path_of_Providence, Cavern_of_Corrosion_Path_of_Holy_Hymn, Cavern_of_Corrosion_Path_of_Conflagration, Cavern_of_Corrosion_Path_of_Elixir_Seekers
    Dungeon_NameAtDoubleCalyx = 'Calyx_Golden_Treasures'  # do_not_participate, Calyx_Golden_Memories, Calyx_Golden_Aether, Calyx_Golden_Treasures, Calyx_Crimson_Destruction, Calyx_Crimson_Preservation, Calyx_Crimson_The_Hunt, Calyx_Crimson_Abundance, Calyx_Crimson_Erudition, Calyx_Crimson_Harmony, Calyx_Crimson_Nihility
    Dungeon_NameAtDoubleRelic = 'Cavern_of_Corrosion_Path_of_Providence'  # do_not_participate, Cavern_of_Corrosion_Path_of_Gelid_Wind, Cavern_of_Corrosion_Path_of_Jabbing_Punch, Cavern_of_Corrosion_Path_of_Drifting, Cavern_of_Corrosion_Path_of_Providence, Cavern_of_Corrosion_Path_of_Holy_Hymn, Cavern_of_Corrosion_Path_of_Conflagration, Cavern_of_Corrosion_Path_of_Elixir_Seekers
    Dungeon_Team = 1  # 1, 2, 3, 4, 5, 6

    # Group `DungeonDaily`
    DungeonDaily_CalyxGolden = 'Calyx_Golden_Treasures'  # do_not_achieve, Calyx_Golden_Memories, Calyx_Golden_Aether, Calyx_Golden_Treasures
    DungeonDaily_CalyxCrimson = 'Calyx_Crimson_Erudition'  # do_not_achieve, Calyx_Crimson_Destruction, Calyx_Crimson_Preservation, Calyx_Crimson_The_Hunt, Calyx_Crimson_Abundance, Calyx_Crimson_Erudition, Calyx_Crimson_Harmony, Calyx_Crimson_Nihility
    DungeonDaily_StagnantShadow = 'Stagnant_Shadow_Quanta'  # do_not_achieve, Stagnant_Shadow_Quanta, Stagnant_Shadow_Gust, Stagnant_Shadow_Fulmination, Stagnant_Shadow_Blaze, Stagnant_Shadow_Spike, Stagnant_Shadow_Rime, Stagnant_Shadow_Mirage, Stagnant_Shadow_Icicle, Stagnant_Shadow_Doom, Stagnant_Shadow_Puppetry, Stagnant_Shadow_Abomination, Stagnant_Shadow_Celestial
    DungeonDaily_CavernOfCorrosion = 'Cavern_of_Corrosion_Path_of_Providence'  # do_not_achieve, Cavern_of_Corrosion_Path_of_Gelid_Wind, Cavern_of_Corrosion_Path_of_Jabbing_Punch, Cavern_of_Corrosion_Path_of_Drifting, Cavern_of_Corrosion_Path_of_Providence, Cavern_of_Corrosion_Path_of_Holy_Hymn, Cavern_of_Corrosion_Path_of_Conflagration, Cavern_of_Corrosion_Path_of_Elixir_Seekers

    # Group `DungeonSupport`
    DungeonSupport_Use = 'when_daily'  # always_use, when_daily, do_not_use
    DungeonSupport_Character = 'FirstCharacter'  # FirstCharacter, Arlan, Asta, Bailu, Blade, Bronya, Clara, DanHeng, DanHengImbibitorLunae, FuXuan, Gepard, Herta, Himeko, Hook, JingYuan, Kafka, Luka, Luocha, Lynx, March7th, Natasha, Pela, Qingque, Sampo, Seele, Serval, SilverWolf, Sushang, Tingyun, TrailblazerDestruction, TrailblazerPreservation, Welt, Yanqing, Yukong

    # Group `DungeonStorage`
    DungeonStorage_TrailblazePower = {}
    DungeonStorage_DungeonDouble = {}
    DungeonStorage_EchoOfWar = {}
    DungeonStorage_SimulatedUniverse = {}

    # Group `Weekly`
    Weekly_Name = 'Echo_of_War_Divine_Seed'  # Echo_of_War_Destruction_Beginning, Echo_of_War_End_of_the_Eternal_Freeze, Echo_of_War_Divine_Seed
    Weekly_Team = 1  # 1, 2, 3, 4, 5, 6

    # Group `AchievableQuest`
    AchievableQuest_Complete_1_Daily_Mission = 'achievable'  # achievable, not_set, not_supported
    AchievableQuest_Clear_Calyx_Golden_1_times = 'achievable'  # achievable, not_set, not_supported
    AchievableQuest_Complete_Calyx_Crimson_1_time = 'achievable'  # achievable, not_set, not_supported
    AchievableQuest_Clear_Stagnant_Shadow_1_times = 'achievable'  # achievable, not_set, not_supported
    AchievableQuest_Clear_Cavern_of_Corrosion_1_times = 'achievable'  # achievable, not_set, not_supported
    AchievableQuest_In_a_single_battle_inflict_3_Weakness_Break_of_different_Types = 'achievable'  # achievable, not_set, not_supported
    AchievableQuest_Inflict_Weakness_Break_5_times = 'achievable'  # achievable, not_set, not_supported
    AchievableQuest_Defeat_a_total_of_20_enemies = 'achievable'  # achievable, not_set, not_supported
    AchievableQuest_Enter_combat_by_attacking_enemy_Weakness_and_win_3_times = 'achievable'  # achievable, not_set, not_supported
    AchievableQuest_Use_Technique_2_times = 'achievable'  # achievable, not_set, not_supported
    AchievableQuest_Go_on_assignment_1_time = 'achievable'  # achievable, not_set, not_supported
    AchievableQuest_Take_1_photo = 'achievable'  # achievable, not_set, not_supported
    AchievableQuest_Destroy_3_destructible_objects = 'achievable'  # achievable, not_set, not_supported
    AchievableQuest_Complete_Forgotten_Hall_1_time = 'achievable'  # achievable, not_set, not_supported
    AchievableQuest_Complete_Echo_of_War_1_times = 'achievable'  # achievable, not_set, not_supported
    AchievableQuest_Complete_1_stage_in_Simulated_Universe_Any_world = 'achievable'  # achievable, not_set, not_supported
    AchievableQuest_Obtain_victory_in_combat_with_support_characters_1_time = 'achievable'  # achievable, not_set, not_supported
    AchievableQuest_Use_an_Ultimate_to_deal_the_final_blow_1_time = 'achievable'  # achievable, not_set, not_supported
    AchievableQuest_Level_up_any_character_1_time = 'achievable'  # achievable, not_set, not_supported
    AchievableQuest_Level_up_any_Light_Cone_1_time = 'achievable'  # achievable, not_set, not_supported
    AchievableQuest_Level_up_any_Relic_1_time = 'achievable'  # achievable, not_set, not_supported
    AchievableQuest_Salvage_any_Relic = 'achievable'  # achievable, not_set, not_supported
    AchievableQuest_Synthesize_Consumable_1_time = 'achievable'  # achievable, not_set, not_supported
    AchievableQuest_Synthesize_material_1_time = 'achievable'  # achievable, not_set, not_supported
    AchievableQuest_Use_Consumables_1_time = 'achievable'  # achievable, not_set, not_supported

    # Group `DailyStorage`
    DailyStorage_DailyActivity = {}
    DailyStorage_DailyQuest = {}

    # Group `BattlePassStorage`
    BattlePassStorage_BattlePassLevel = {}
    BattlePassStorage_BattlePassTodayQuest = {}

    # Group `Assignment`
    Assignment_Name_1 = 'Nameless_Land_Nameless_People'  # Nine_Billion_Names, Destruction_of_the_Destroyer, Winter_Soldiers, Born_to_Obey, Root_Out_the_Turpitude, Fire_Lord_Inflames_Blades_of_War, Nameless_Land_Nameless_People, Akashic_Records, The_Invisible_Hand, Abandoned_and_Insulted, Spring_of_Life, The_Land_of_Gold, The_Blossom_in_the_Storm, Legend_of_the_Puppet_Master, The_Wages_of_Humanity
    Assignment_Name_2 = 'Akashic_Records'  # Nine_Billion_Names, Destruction_of_the_Destroyer, Winter_Soldiers, Born_to_Obey, Root_Out_the_Turpitude, Fire_Lord_Inflames_Blades_of_War, Nameless_Land_Nameless_People, Akashic_Records, The_Invisible_Hand, Abandoned_and_Insulted, Spring_of_Life, The_Land_of_Gold, The_Blossom_in_the_Storm, Legend_of_the_Puppet_Master, The_Wages_of_Humanity
    Assignment_Name_3 = 'The_Invisible_Hand'  # Nine_Billion_Names, Destruction_of_the_Destroyer, Winter_Soldiers, Born_to_Obey, Root_Out_the_Turpitude, Fire_Lord_Inflames_Blades_of_War, Nameless_Land_Nameless_People, Akashic_Records, The_Invisible_Hand, Abandoned_and_Insulted, Spring_of_Life, The_Land_of_Gold, The_Blossom_in_the_Storm, Legend_of_the_Puppet_Master, The_Wages_of_Humanity
    Assignment_Name_4 = 'Nine_Billion_Names'  # Nine_Billion_Names, Destruction_of_the_Destroyer, Winter_Soldiers, Born_to_Obey, Root_Out_the_Turpitude, Fire_Lord_Inflames_Blades_of_War, Nameless_Land_Nameless_People, Akashic_Records, The_Invisible_Hand, Abandoned_and_Insulted, Spring_of_Life, The_Land_of_Gold, The_Blossom_in_the_Storm, Legend_of_the_Puppet_Master, The_Wages_of_Humanity
    Assignment_Duration = 20  # 4, 8, 12, 20
    Assignment_Event = True
    Assignment_Assignment = {}

    # Group `ItemStorage`
    ItemStorage_Credit = {}
    ItemStorage_StallerJade = {}

    # Group `RoguePath`
    RoguePath_Path = 'The_Hunt'  # Preservation, Remembrance, Nihility, Abundance, The_Hunt, Destruction, Elation
    RoguePath_DomainStrategy = 'combat'  # combat, occurrence
    RoguePath_Bonus = 'Blessing Cosmos'  # Blessing Cosmos, Miracle Cosmos, Fragmented Cosmos
    RoguePath_PresetResonanceFilter = 'preset-1'  # preset-1, custom
    RoguePath_ResonanceSelectionStrategy = 'follow-presets'  # follow-presets, unrecorded-first, before-random
    RoguePath_CustomResonanceFilter = '回响构音：均晶转变 > 回响构音：零维强化\n> 回响构音：第二次初恋 > 回响构音：体验的富翁\n> 回响构音：局外人 > 回响构音：怀疑的四重根\n> 回响构音：诸法无我 > 回响构音：诸行无常\n> 回响构音：射不主皮 > 回响构音：柘弓危矢\n> 回响构音：激变变星 > 回响构音：极端氦闪\n> 回响构音：末日狂欢 > 回响构音：树苗长高舞'

    # Group `RogueBlessing`
    RogueBlessing_PresetBlessingFilter = 'preset-1'  # preset-1, custom
    RogueBlessing_BlessingSelectionStrategy = 'follow-presets'  # follow-presets, unrecorded-first, before-random
    RogueBlessing_CustomBlessingFilter = '巡猎-3 > 《冠军晚餐·猫的摇篮》 > 丰饶众生，一法界心 > 毁灭-3 \n> 火堆外的夜 > 巡猎-2 > 毁灭-2 > 巡猎 > reset > random'

    # Group `RogueCurio`
    RogueCurio_PresetCurioFilter = 'preset-1'  # preset-1, custom
    RogueCurio_CurioSelectionStrategy = 'follow-presets'  # follow-presets, unrecorded-first, before-random
    RogueCurio_CustomCurioFilter = '博士之袍 > 福灵胶 > 分裂金币 > 信仰债券 > 换境桂冠 > 俱乐部券 > 碎星芳饵 > random'
