import pyxel
import random

# Game States
STATE_TITLE = 0
STATE_FIELD = 1
STATE_TOWN = 2
STATE_MENU = 3
STATE_BATTLE = 4
STATE_GAMEOVER = 5
STATE_GAMECLEAR = 6

# Tile Types
TILE_GRASS = 0
TILE_FOREST = 1
TILE_MOUNTAIN = 2
TILE_WATER = 3
TILE_CASTLE = 4
TILE_TOWN = 5
TILE_FLOOR = 6
TILE_WALL = 7
TILE_BRIDGE = 8
TILE_SAND = 9
TILE_LAVA = 10
TILE_SNOW = 11
TILE_CHEST_CLOSED = 12
TILE_CHEST_OPEN = 13
TILE_NPC = 14
TILE_BOSS = 15 # Added Boss Tile

# Map Data - Expanded World Map
# 0:Grass, 1:Forest, 2:Mountain, 3:Water, 4:Castle, 5:Town, 8:Bridge, 9:Sand, L:Lava, S:Snow, B:Boss
FIELD_MAP = [
    "3333333333333333333333333333333333333333333333333333333333333333",
    "33SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS33",
    "33SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS33",
    "33SSSSSS22222222SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS33",
    "33SSSSSS2SSSSSS22SSSSSSSSSSSSS222222SSSSSSSSSSSSSSSSSSSSSSSSSS33",
    "33SSSSSS2SS5SSS122SSSSSSSSSSS22111122SSSSSSSSSSSSSSSSSSSSSSSSS33",
    "33SSSSSS2SSSSSS1122SSSSSSSSS2211111122SSSSSSSSSSSSSSSSSSSSSSSS33",
    "33SSSSSS222222211122SSSSSSS221111111122SSSSSSSSSSSSSSSSSSSSSSS33",
    "33SSSSSSSSS1111111122SSSSS22111111111122SSSSSSSSSSSSSSSSSSSSSS33",
    "33SSSSSSSSSS1111111122SSS2211111111111122SSSSSSSSSSSSSSSSSSSSS33",
    "33333333333321111111122S2211111111111111223333333333333333333333",
    "3333333333322111111111222211111111111111122333333333333333333333",
    "3333333333221111111111122111111111111111112233333333333333333333",
    "3333333332211111111111111111111111111111111223333333333333333333",
    "3333333322111111111111111111111111111111111122333333333333333333",
    "3333333221111111111111111111111111111111111112233333333333333333",
    "3333332211111111111111000000001111111111111111223333333333333333",
    "3333322111111111111110000000000111111111111111122333333333333333",
    "3333221111111111111100000000000011111111111111111223333333333333",
    "3332211111111111111100000088880001111111111111111223333333333333",
    "3322111111111111111000088888888000111111111111111122333333333333",
    "3321111111111111111000088888888000111111111111111112233333333333",
    "3221111111111111111000000088880000111111111111111111223333333333",
    "3211111111111111111000000000000001111111111111111111122333333333",
    "3211111111111111111100000000000011111111111111111111112333333333",
    "3211111111111111111110000000000111111111111111111111112333333333",
    "3221111111111111111111111111111111111111111111111111122333333333",
    "3322111111111111111111111111111111111111111111111111223333333333",
    "3332211111111111111111111111111111111111111111111112233333333333",
    "3333221111111111111111111111111111111111111111111122333333333333",
    "3333322211111111111111111111111111111111111111112223333333333333",
    "3333333222211111111111111111111111111111111112222333333333333333",
    "3333333333222221111111111111111111111111122222333333333333333333",
    "3333333333333322222211111111111111112222223333333333333333333333",
    "3333333333333333333222211111111112222333333333333333333333333333",
    "3333333333333333333333220000000022333333333333333333333333333333",
    "3333333333333333333333330088880033333333333333333333333333333333",
    "3333333333333333333333330088880033333333333333333333333333333333",
    "3333333333333333333333330088880033333333333333333333333333333333",
    "3333333333333333333333330088880033333333333333333333333333333333",
    "3333333333333333333333330088880033333333333333333333333333333333",
    "3333333333333333333333330088880033333333333333333333333333333333",
    "3333333333333333333333330088880033333333333333333333333333333333",
    "3333333333333333333333330088880033333333333333333333333333333333",
    "3333333333333333333333330088880033333333333333333333333333333333",
    "3333333333333333333333330088880033333333333333333333333333333333",
    "3333333333333333333333330088880033333333333333333333333333333333",
    "3333333333333333333333330088880033333333333333333333333333333333",
    "3333333333333333333333330088880033333333333333333333333333333333",
    "3333333333333333333333330088880033333333333333333333333333333333",
    "3333333333333333333333330088880033333333333333333333333333333333",
    "3333333333333333333333330088880033333333333333333333333333333333",
    "3333333333333333333333330088880033333333333333333333333333333333",
    "3333333333333333333333330088880033333333333333333333333333333333",
    "3333338888888888888888880088880088888888888888880088880033333333",
    "3333399999993333333333330088880033333333333333330088880033333333",
    "33339999119993333333333300888800333333333333333LLLLLL33333333333",
    "3333999915199933333333330088880033333333333333LLLLLLL33333333333",
    "333399991199933333333333008888003333333333333LLLLLLLL33333333333",
    "33333999999933333333333333000033333333333333LLLL4LLL333333333333",
    "33333399999333333333333333333333333333333333LLLLLLL333333333333",
    "333333333333333333333333333333333333333333333LLLLLB333333333333",
    "3333333333333333333333333333333333333333333333333333333333333333",
    "3333333333333333333333333333333333333333333333333333333333333333",
    "3333333333333333333333333333333333333333333333388888888883333333",
    "333333333333333333333333333333333333333333333338LLLLLB3333333333",
    "333333333333333333333333333333333333333333333338LLLLLL3333333333",
]

MAP_WIDTH = len(FIELD_MAP[0])
MAP_HEIGHT = len(FIELD_MAP)

# Town Map Data (16x16)
TOWN_MAP = [
    "7777777777777777",
    "7666766667666667",
    "7666766667666667",
    "7666666666666667",
    "7666666666666667",
    "7666667776666667",
    "7666667676666667",
    "7666667676666667",
    "7776777777776777",
    "0076700000076700",
    "0076700000076700",
    "0076777777776700",
    "0076666666666700",
    "0077777667777700",
    "0000000660000000",
    "0000000660000000",
]
TOWN_WIDTH = len(TOWN_MAP[0])
TOWN_HEIGHT = len(TOWN_MAP)

class Spell:
    def __init__(self, name, mp_cost, effect_type, power):
        self.name = name
        self.mp_cost = mp_cost
        self.effect_type = effect_type # 'heal', 'damage'
        self.power = power

# Global Spells
SPELL_HEAL = Spell("Heal", 3, 'heal', 30)
SPELL_FIRE = Spell("Fire", 4, 'damage', 20)

class Character:
    def __init__(self, name, hp, mp, attack, defense, spd, spells=None):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.attack = attack
        self.defense = defense
        self.spd = spd
        self.level = 1
        self.exp = 0
        self.gold = 0
        self.spells = spells if spells else []
        self.update_stats()

    def update_stats(self):
        # Calculate level based on EXP
        new_level = 1 + (self.exp // 20)
        if new_level > self.level:
            diff = new_level - self.level
            self.level = new_level
            self.max_hp += 5 * diff
            self.max_mp += 2 * diff
            self.attack += 2 * diff
            self.defense += 2 * diff
            self.hp = self.max_hp
            self.mp = self.max_mp
            return True
        return False

class Monster:
    def __init__(self, name, hp, attack, defense, exp_yield, gold_yield):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.exp_yield = exp_yield
        self.gold_yield = gold_yield

class Item:
    def __init__(self, name, effect_type, power, amount=0):
        self.name = name
        self.effect_type = effect_type # 'heal_hp', 'heal_mp'
        self.power = power
        self.amount = amount

class Chest:
    def __init__(self, x, y, item=None, gold=0):
        self.x = x
        self.y = y
        self.item = item
        self.gold = gold
        self.opened = False

class NPC:
    def __init__(self, x, y, name, messages, is_moving=False, face_id=0):
        self.x = x
        self.y = y
        self.name = name
        self.messages = messages
        self.is_moving = is_moving
        self.move_timer = 0
        self.face_id = face_id # 0: Blue, 1: Red, 2: Green...

    def update(self, app):
        if not self.is_moving:
            return

        self.move_timer += 1
        if self.move_timer > 30: # Move every 30 frames
            self.move_timer = 0
            dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)])
            nx, ny = self.x + dx, self.y + dy
            
            # Check collision with walls, player, and other NPCs
            if app.is_passable(nx, ny, "town"):
                # Don't walk into player
                if nx != app.tx or ny != app.ty:
                    # Check if another NPC is there
                    occupied = False
                    for other in app.npcs:
                        if other != self and other.x == nx and other.y == ny:
                            occupied = True
                            break
                    if not occupied:
                        self.x, self.y = nx, ny

class App:
    def __init__(self):
        pyxel.init(256, 256, title="Pyxel RPG Prototype")
        
        self.state = STATE_TITLE
        
        # Player coordinates
        self.px = 20
        self.py = 10
        
        self.save_px = 13
        self.save_py = 3
        
        # Dialog State
        self.dialog_text = []
        self.is_dialog_active = False
        self.active_npc = None # Track who we are talking to
        
        # Acquisition Display (Right Top)
        self.acquisition_text = ""
        self.acquisition_timer = 0 # Frames to show the notification

        # Town coordinates
        self.tx = 7
        self.ty = 14
        
        self.facing = 0 # 0: down, 1: up, 2: left, 3: right
        
        self.party = [
            Character("Yusha", 30, 0, 10, 5, 8),
            Character("Saru", 25, 15, 7, 4, 10, [SPELL_FIRE]),
            Character("Mimi", 18, 25, 4, 3, 12, [SPELL_HEAL])
        ]
        
        self.inventory = [
            Item("Herb", "heal_hp", 30, 3),
            Item("MagicWater", "heal_mp", 15, 1)
        ]
        
        # World Objects
        self.chests = [
             Chest(56, 81, None, 500), # Lava Island
             Chest(8, 72, Item("MagicWater", "heal_mp", 15, 1)), # Desert Island
             Chest(12, 12, Item("Herb", "heal_hp", 30, 1)), # Starting area
             Chest(30, 40, Item("MagicWater", "heal_mp", 15, 1)), # Mid-world forest
             Chest(5, 5, Item("Herb", "heal_hp", 30, 1)), # Snow mountain corner
        ]
        
        # Town Chests
        self.town_chests = [
             Chest(1, 1, Item("Herb", "heal_hp", 30, 1)), # Town corner
             Chest(14, 1, Item("MagicWater", "heal_mp", 15, 1)), # Another corner
        ]

        self.npcs = [
            NPC(8, 6, "Villager", ["Welcome to our town!", "The desert island to the SW is hot,", "but the lava island to the SE is DEADLY!"], True, 0),
            NPC(13, 2, "Elder", ["To defeat the Demon Lord in the lava region,", "you must train well in the snow mountains."], False, 1),
            NPC(3, 3, "Guard", ["The castle is to the north.", "Rest there to recover your HP and MP."], False, 2),
            NPC(12, 12, "Girl", ["I love the white snow in the north!", "Have you seen the Snow Ghost?"], True, 3),
            NPC(5, 10, "Merchant", ["I have no items to sell right now...", "But you can find treasures in the islands!"], False, 0)
        ]
        
        self.is_boss_battle = False
        self.title_frame = 0 # Animation counter for title
        
        # Menu state

        self.menu_mode = "main" # main, items, magic, target
        self.menu_cursor = 0
        self.sub_cursor = 0
        self.target_cursor = 0
        self.selected_item_or_spell = None
        self.active_char = None
        
        # Battle State
        self.battle_phase = 0
        self.current_monster = None
        self.battle_messages = []
        self.battle_cursor = 0
        self.active_character_idx = 0
        self.character_commands = []
        
        self.camera_x = 0
        self.camera_y = 0

        # Optimization: Pre-convert map strings to Pyxel's Tilemap for FAST rendering
        # Tilemap 0 for World Map, Tilemap 1 for Town Map
        for r_idx, row in enumerate(FIELD_MAP):
            for c_idx, char in enumerate(row):
                try:
                    if char == "L":
                        val = TILE_LAVA
                    elif char == "S":
                        val = TILE_SNOW
                    else:
                        val = int(char)
                    # Pyxel tilemap.set takes a list of strings like "XXYY" in hex
                    # XX is tile x, YY is tile y (0-255)
                    # Our tiles are at (val, 0) in the 32x32 tile grid
                    tile_hex = f"{val:02x}00"
                    pyxel.tilemaps[0].set(c_idx, r_idx, [tile_hex])
                except (ValueError, IndexError):
                    pyxel.tilemaps[0].set(c_idx, r_idx, ["0000"])

        for r_idx, row in enumerate(TOWN_MAP):
            for c_idx, char in enumerate(row):
                try:
                    val = int(char)
                    tile_hex = f"{val:02x}00"
                    pyxel.tilemaps[1].set(c_idx, r_idx, [tile_hex])
                except (ValueError, IndexError):
                    pyxel.tilemaps[1].set(c_idx, r_idx, ["0000"])


        self.create_graphics()
        pyxel.run(self.update, self.draw)


        
    def create_graphics(self):
        # 0: Grass
        pyxel.images[0].rect(0, 0, 8, 8, 3) 
        pyxel.images[0].pset(1, 1, 11)
        pyxel.images[0].pset(5, 4, 11)
        # 1: Forest
        pyxel.images[0].rect(8, 0, 8, 8, 3)
        pyxel.images[0].circ(11, 4, 3, 11)
        pyxel.images[0].pset(11, 4, 3)
        # 2: Mountain
        pyxel.images[0].rect(16, 0, 8, 8, 4)
        pyxel.images[0].tri(16, 8, 20, 0, 24, 8, 13)
        # 3: Water
        pyxel.images[0].rect(24, 0, 8, 8, 1)
        pyxel.images[0].line(24, 2, 31, 2, 5)
        pyxel.images[0].line(24, 6, 31, 6, 5)
        # 4: Castle
        pyxel.images[0].rect(32, 0, 8, 8, 3)
        pyxel.images[0].rect(33, 1, 6, 7, 7)
        pyxel.images[0].rect(34, 4, 4, 4, 0)
        # 5: Town
        pyxel.images[0].rect(40, 0, 8, 8, 3)
        pyxel.images[0].rect(41, 3, 6, 5, 8)
        pyxel.images[0].tri(40, 3, 44, 0, 48, 3, 8)
        # 6: Town Floor
        pyxel.images[0].rect(48, 0, 8, 8, 9)
        pyxel.images[0].pset(49, 1, 4)
        pyxel.images[0].pset(53, 5, 4)
        # 7: Town Wall
        pyxel.images[0].rect(56, 0, 8, 8, 13)
        pyxel.images[0].line(56, 3, 63, 3, 0)
        pyxel.images[0].line(56, 7, 63, 7, 0)
        # 8: Bridge
        pyxel.images[0].rect(64, 0, 8, 8, 6)
        pyxel.images[0].rect(64, 2, 8, 1, 5)
        pyxel.images[0].rect(64, 5, 8, 1, 5)
        # 9: Sand (Desert)
        pyxel.images[0].rect(72, 0, 8, 8, 10)
        pyxel.images[0].pset(73, 2, 9)
        pyxel.images[0].pset(76, 5, 9)
        # 10: Lava
        pyxel.images[0].rect(80, 0, 8, 8, 8)
        pyxel.images[0].line(80, 2, 87, 2, 2)
        pyxel.images[0].line(80, 6, 87, 6, 2)
        # 11: Snow
        pyxel.images[0].rect(88, 0, 8, 8, 7)
        pyxel.images[0].pset(89, 1, 13)
        pyxel.images[0].pset(93, 5, 13)
        # 12: Treasure Chest (Closed)
        pyxel.images[0].rect(96, 0, 8, 8, 0)
        pyxel.images[0].rect(97, 2, 6, 5, 9) # Brown box
        pyxel.images[0].rect(97, 2, 6, 2, 4) # Lid top
        pyxel.images[0].pset(100, 4, 10) # Yellow lock
        # 13: Treasure Chest (Open)
        pyxel.images[0].rect(104, 0, 8, 8, 0)
        pyxel.images[0].rect(105, 4, 6, 3, 9)
        # 14: NPC (Blue Outfit)
        pyxel.images[0].rect(112, 0, 8, 8, 0)
        pyxel.images[0].rect(114, 1, 4, 3, 15) # Face
        pyxel.images[0].rect(114, 4, 4, 4, 12) # Blue body
        
        # Face Portraits (Bank 2, 0, 0)
        # 0: Blue Villager
        pyxel.images[2].rect(0, 0, 32, 32, 0)
        pyxel.images[2].rect(4, 4, 24, 24, 12) # Blue hood
        pyxel.images[2].rect(8, 8, 16, 16, 15) # Face
        pyxel.images[2].pset(12, 14, 0); pyxel.images[2].pset(20, 14, 0) # Eyes
        # 1: Red Elder
        pyxel.images[2].rect(32, 0, 32, 32, 0)
        pyxel.images[2].rect(36, 4, 24, 24, 8) # Red hood
        pyxel.images[2].rect(40, 8, 16, 16, 15) # Face
        pyxel.images[2].rect(42, 20, 12, 4, 7) # Beard
        # 2: Green Guard
        pyxel.images[2].rect(64, 0, 32, 32, 0)
        pyxel.images[2].rect(68, 4, 24, 24, 3) # Green helmet
        pyxel.images[2].rect(72, 8, 16, 16, 15) # Face
        pyxel.images[2].rect(72, 4, 16, 6, 13) # Steel visor
        # 3: Pink Girl
        pyxel.images[2].rect(96, 0, 32, 32, 0)
        pyxel.images[2].rect(100, 4, 24, 24, 14) # Pink hair
        pyxel.images[2].rect(104, 8, 16, 16, 15) # Face
        pyxel.images[2].pset(108, 14, 0); pyxel.images[2].pset(116, 14, 0) # Eyes
        
        # Player (offset Y=8)
        pyxel.images[0].rect(0, 8, 8, 8, 0)
        pyxel.images[0].rect(2, 9, 4, 3, 14)
        pyxel.images[0].rect(2, 12, 4, 4, 8)
        
        # Monsters (Start at Y=24, X=0 in Image Bank 0)
        # Using 24x24 area for higher quality
        # Slime (0, 24)
        pyxel.images[0].rect(0, 24, 24, 24, 0)
        pyxel.images[0].circ(12, 40, 7, 12); pyxel.images[0].rect(5, 40, 14, 8, 12) # Body
        pyxel.images[0].pset(10, 38, 7); pyxel.images[0].pset(14, 38, 7) # Eyes
        # Bat (24, 24)
        pyxel.images[0].rect(24, 24, 24, 24, 0)
        pyxel.images[0].circ(36, 36, 4, 13) # Body
        pyxel.images[0].tri(24, 32, 32, 36, 32, 40, 5); pyxel.images[0].tri(48, 32, 40, 36, 40, 40, 5) # Wings
        pyxel.images[0].pset(34, 35, 8); pyxel.images[0].pset(38, 35, 8) # Eyes
        # Goblin (48, 24)
        pyxel.images[0].rect(48, 24, 24, 24, 0)
        pyxel.images[0].circ(60, 32, 6, 3); pyxel.images[0].rect(56, 36, 8, 10, 3) # Head & Body
        pyxel.images[0].rect(50, 38, 4, 2, 3); pyxel.images[0].rect(66, 38, 4, 2, 3) # Arms
        pyxel.images[0].pset(58, 30, 10); pyxel.images[0].pset(62, 30, 10) # Eyes
        # Scorpion (72, 24)
        pyxel.images[0].rect(72, 24, 24, 24, 0)
        pyxel.images[0].rect(78, 38, 12, 6, 9) # Body
        pyxel.images[0].line(84, 38, 84, 30, 9); pyxel.images[0].line(84, 30, 88, 30, 8) # Tail
        pyxel.images[0].rect(74, 36, 4, 4, 8); pyxel.images[0].rect(90, 36, 4, 4, 8) # Pincers
        # Cactus (96, 24)
        pyxel.images[0].rect(96, 24, 24, 24, 0)
        pyxel.images[0].rect(106, 30, 4, 16, 3) # Trunk
        pyxel.images[0].rect(100, 36, 6, 2, 3); pyxel.images[0].rect(110, 34, 6, 2, 3) # Arms
        # FireSpirit (120, 24)
        pyxel.images[0].rect(120, 24, 24, 24, 0)
        pyxel.images[0].circ(132, 38, 6, 8); pyxel.images[0].tri(126, 38, 132, 26, 138, 38, 10) # Flame
        # LavaGolem (144, 24)
        pyxel.images[0].rect(144, 24, 24, 24, 0)
        pyxel.images[0].rect(148, 28, 16, 16, 2); pyxel.images[0].rect(152, 32, 8, 8, 8) # Rock & Core
        # RedDragon (168, 24)
        pyxel.images[0].rect(168, 24, 24, 24, 0)
        pyxel.images[0].rect(172, 34, 16, 10, 8); pyxel.images[0].tri(168, 28, 172, 34, 168, 40, 8) # Body & Head
        pyxel.images[0].line(180, 34, 175, 26, 10); pyxel.images[0].line(184, 34, 189, 26, 10) # Horns
        # Yeti (192, 24)
        pyxel.images[0].rect(192, 24, 24, 24, 0)
        pyxel.images[0].circ(204, 36, 9, 7); pyxel.images[0].pset(200, 34, 0); pyxel.images[0].pset(208, 34, 0) # White Fur
        # IceWolf (216, 24)
        pyxel.images[0].rect(216, 24, 24, 24, 0)
        pyxel.images[0].rect(220, 36, 14, 8, 12); pyxel.images[0].tri(228, 36, 234, 28, 240, 36, 12) # Fur & Head
        # SnowGhost (240, 24)
        pyxel.images[0].rect(240, 24, 24, 24, 0)
        pyxel.images[0].circ(252, 36, 8, 13); pyxel.images[0].pset(248, 34, 12); pyxel.images[0].pset(256, 34, 12) # Ghost

        # DEMON LORD (Bank 1, 64, 0) - Huge 32x32 Boss
        pyxel.images[1].rect(64, 0, 32, 32, 0)
        pyxel.images[1].rect(70, 10, 20, 20, 2) # Dark body
        pyxel.images[1].tri(64, 0, 75, 15, 64, 32, 8) # Left Wing
        pyxel.images[1].tri(96, 0, 85, 15, 96, 32, 8) # Right Wing
        pyxel.images[1].rect(76, 15, 3, 3, 10); pyxel.images[1].rect(82, 15, 3, 3, 10) # Glowing eyes
        pyxel.images[1].rect(78, 22, 5, 2, 8) # Mouth



        # Custom Large Font for Title (R, P, G, .) in Image Bank 1
        # Each char is 16x16
        pyxel.images[1].rect(0, 0, 64, 16, 0) # Clear area
        # R with a hole
        pyxel.images[1].rect(2, 2, 4, 12, 10)
        pyxel.images[1].rect(2, 2, 10, 4, 10)
        pyxel.images[1].rect(10, 2, 4, 8, 10)
        pyxel.images[1].rect(2, 6, 10, 4, 10)
        pyxel.images[1].line(6, 10, 12, 14, 10)
        pyxel.images[1].line(7, 10, 13, 14, 10)
        pyxel.images[1].rect(4, 4, 2, 2, 0) # Black hole in R
        # . (dot)
        pyxel.images[1].rect(18, 12, 2, 2, 10)
        # P with a hole
        pyxel.images[1].rect(34, 2, 4, 12, 10)
        pyxel.images[1].rect(34, 2, 10, 4, 10)
        pyxel.images[1].rect(42, 2, 4, 8, 10)
        pyxel.images[1].rect(34, 6, 10, 4, 10)
        pyxel.images[1].rect(36, 4, 2, 2, 0) # Black hole in P
        # G with holes
        pyxel.images[1].rect(50, 2, 12, 4, 10)
        pyxel.images[1].rect(50, 2, 4, 12, 10)
        pyxel.images[1].rect(50, 10, 12, 4, 10)
        pyxel.images[1].rect(58, 8, 4, 6, 10)
        pyxel.images[1].rect(54, 8, 6, 2, 10)
        pyxel.images[1].rect(54, 8, 2, 2, 0) # Black hole in G (at line 8)
        pyxel.images[1].rect(54, 9, 2, 2, 0) # Black hole in G (at line 9)

    def is_passable(self, tx, ty, m_type="field"):
        if m_type == "field":
            if tx < 0 or tx >= MAP_WIDTH or ty < 0 or ty >= MAP_HEIGHT: return False
            # Get tile from Tilemap 0
            # pget returns (u, v) in tile units
            u, v = pyxel.tilemaps[0].pget(tx, ty)
            return u not in (TILE_MOUNTAIN, TILE_WATER) or u == TILE_BRIDGE or u == TILE_BOSS
        elif m_type == "town":
            if tx < 0 or tx >= TOWN_WIDTH or ty < 0 or ty >= TOWN_HEIGHT: return False
            u, v = pyxel.tilemaps[1].pget(tx, ty)
            return u != TILE_WALL

    def start_boss_battle(self):
        self.current_monster = Monster("DEMON LORD", 500, 40, 30, 0, 0)
        self.is_boss_battle = True
        self.state = STATE_BATTLE
        self.battle_phase = 0
        self.battle_messages = ["The ground shakes...", "DEMON LORD appears!"]
        self.character_commands = []
        self.active_character_idx = 0
        self.menu_mode = "main"
        self.battle_cursor = 0

    def trigger_random_encounter(self):
        # Get current tile from Tilemap 0
        u, v = pyxel.tilemaps[0].pget(self.px, self.py)
        tile = u
        
        if random.random() < 0.05:
            monsters = [
                Monster("Slime", 15, 7, 2, 5, 10),
                Monster("Bat", 18, 9, 3, 8, 15),
                Monster("Goblin", 25, 12, 5, 12, 25)
            ]
            
            # Area specific monsters
            if tile == TILE_SAND:
                monsters.append(Monster("Scorpion", 30, 15, 8, 20, 40))
                monsters.append(Monster("Cactus", 20, 10, 15, 15, 30))
            elif tile == TILE_LAVA:
                monsters = [
                    Monster("FireSpirit", 40, 18, 10, 30, 50),
                    Monster("LavaGolem", 60, 22, 20, 50, 100),
                    Monster("RedDragon", 100, 30, 25, 200, 500)
                ]
            elif tile == TILE_SNOW:
                monsters = [
                    Monster("Yeti", 45, 20, 12, 40, 60),
                    Monster("IceWolf", 35, 15, 8, 25, 35),
                    Monster("SnowGhost", 25, 12, 30, 35, 45)
                ]

            self.current_monster = random.choice(monsters)
            self.state = STATE_BATTLE
            self.battle_phase = 0
            self.battle_messages = [f"A wild {self.current_monster.name} appeared!"]
            self.character_commands = []
            self.active_character_idx = 0
            self.menu_mode = "main"
            self.battle_cursor = 0


    def update(self):
        # Update acquisition timer
        if self.acquisition_timer > 0:
            self.acquisition_timer -= 1

        if self.state == STATE_TITLE:
            self.title_frame += 1
            if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_Z):
                self.state = STATE_FIELD
                self.title_frame = 0
        elif self.state == STATE_FIELD:
            self.update_field()
        elif self.state == STATE_TOWN:
            self.update_town()
        elif self.state == STATE_MENU:
            self.update_menu()
        elif self.state == STATE_BATTLE:
            self.update_battle()

    def update_field(self):
        if self.is_dialog_active:
            if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN):
                self.is_dialog_active = False
            return

        if pyxel.btnp(pyxel.KEY_X) or pyxel.btnp(pyxel.KEY_ESCAPE):
            self.state = STATE_MENU
            self.menu_mode = "main"
            self.menu_cursor = 0
            return

        moved = False
        nx, ny = self.px, self.py

        if pyxel.btnp(pyxel.KEY_UP): 
            ny -= 1
            self.facing = 1
        elif pyxel.btnp(pyxel.KEY_DOWN): 
            ny += 1
            self.facing = 0
        elif pyxel.btnp(pyxel.KEY_LEFT): 
            nx -= 1
            self.facing = 2
        elif pyxel.btnp(pyxel.KEY_RIGHT): 
            nx += 1
            self.facing = 3

        if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN):
            # Interact with objects in front of the player
            ix, iy = self.px, self.py
            if self.facing == 0: iy += 1
            elif self.facing == 1: iy -= 1
            elif self.facing == 2: ix -= 1
            elif self.facing == 3: ix += 1
            
            for c in self.chests:
                if c.x == ix and c.y == iy and not c.opened:
                    c.opened = True
                    if c.item:
                        self.add_item(Item(c.item.name, c.item.effect_type, c.item.power, c.item.amount))
                        self.show_dialog([f"Found {c.item.name}!"])
                    else:
                        self.party[0].gold += c.gold
                        self.show_acquisition(f"GET: {c.gold} GOLD")
                        self.show_dialog([f"Found {c.gold} GOLD!"])
                    return

        if (nx != self.px or ny != self.py) and self.is_passable(nx, ny, "field"):
            # Check collision with chests on field
            chest_blocked = False
            for c in self.chests:
                if c.x == nx and c.y == ny:
                    chest_blocked = True
                    break
            
            if not chest_blocked:
                self.px, self.py = nx, ny
                moved = True

        if moved:
            u, v = pyxel.tilemaps[0].pget(self.px, self.py)
            tile = u
            if tile == TILE_LAVA:
                for c in self.party:
                    if c.hp > 0:
                        c.hp = max(1, c.hp - 1) # Reduce 1 HP per step on lava (min 1)
            
            # Start Boss Battle if touching boss tile
            if tile == TILE_BOSS:
                self.start_boss_battle()
                return # Don't trigger random encounter on boss tile

            if tile == TILE_CASTLE: # Castle
                for c in self.party:
                    c.hp = c.max_hp
                    c.mp = c.max_mp
            elif tile == TILE_TOWN: # Town
                self.save_px, self.save_py = self.px, self.py
                self.state = STATE_TOWN
                self.tx = 7
                self.ty = 14
            else:
                self.trigger_random_encounter()

        self.camera_x = self.px * 8 - pyxel.width // 2
        self.camera_y = self.py * 8 - pyxel.height // 2


    def update_town(self):
        if self.is_dialog_active:
            if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN):
                self.is_dialog_active = False
            return

        # Update NPCs (moving logic)
        for n in self.npcs:
            n.update(self)

        if pyxel.btnp(pyxel.KEY_X) or pyxel.btnp(pyxel.KEY_ESCAPE):
            self.state = STATE_MENU
            self.menu_mode = "main"
            self.menu_cursor = 0
            return
            
        nx, ny = self.tx, self.ty
        if pyxel.btnp(pyxel.KEY_UP): 
            ny -= 1
            self.facing = 1
        elif pyxel.btnp(pyxel.KEY_DOWN): 
            ny += 1
            self.facing = 0
        elif pyxel.btnp(pyxel.KEY_LEFT): 
            nx -= 1
            self.facing = 2
        elif pyxel.btnp(pyxel.KEY_RIGHT): 
            nx += 1
            self.facing = 3

        if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN):
            # Coordinates for 1 and 2 tiles in front
            ix1, iy1 = self.tx, self.ty
            ix2, iy2 = self.tx, self.ty
            
            if self.facing == 0: # Down
                iy1 += 1
                iy2 += 2
            elif self.facing == 1: # Up
                iy1 -= 1
                iy2 -= 2
            elif self.facing == 2: # Left
                ix1 -= 1
                ix2 -= 2
            elif self.facing == 3: # Right
                ix1 += 1
                ix2 += 2
            
            # Interact with NPCs (within 2 tiles in front, even through walls)
            for n in self.npcs:
                if (n.x == ix1 and n.y == iy1) or (n.x == ix2 and n.y == iy2):
                    self.show_dialog(n.messages, n)
                    return
            
            # Interact with town chests (1 tile in front)
            # Re-using ix1, iy1 for clarity
            for c in self.town_chests:
                if c.x == ix1 and c.y == iy1 and not c.opened:
                    c.opened = True
                    if c.item:
                        self.add_item(Item(c.item.name, c.item.effect_type, c.item.power, c.item.amount))
                        self.show_dialog([f"Found {c.item.name}!"])
                    else:
                        self.party[0].gold += c.gold
                        self.show_acquisition(f"GET: {c.gold} GOLD")
                        self.show_dialog([f"Found {c.gold} GOLD!"])
                    return

        if ny >= TOWN_HEIGHT: # Exit town at bottom
            self.state = STATE_FIELD
            self.px, self.py = self.save_px, self.save_py
            # move player down slightly so they don't immediately re-enter
            if self.is_passable(self.px, self.py+1, "field"): self.py += 1
            return

        if (nx != self.tx or ny != self.ty) and self.is_passable(nx, ny, "town"):
            # Check if moving into an NPC
            occupied = False
            for n in self.npcs:
                if n.x == nx and n.y == ny:
                    occupied = True
                    break
            
            # Check if moving into a town chest
            for c in self.town_chests:
                if c.x == nx and c.y == ny:
                    occupied = True
                    break
            
            if not occupied:
                self.tx, self.ty = nx, ny

        self.camera_x = self.tx * 8 - pyxel.width // 2
        self.camera_y = self.ty * 8 - pyxel.height // 2

    def add_item(self, item):
        for itm in self.inventory:
            if itm.name == item.name:
                itm.amount += item.amount
                self.show_acquisition(f"GET: {item.name}")
                return
        self.inventory.append(item)
        self.show_acquisition(f"GET: {item.name}")

    def show_acquisition(self, text):
        self.acquisition_text = text
        self.acquisition_timer = 60 # Show for 60 frames (approx 2 seconds)

    def show_dialog(self, messages, npc=None):
        self.dialog_text = messages
        self.is_dialog_active = True
        self.active_npc = npc

    def update_menu(self):
        if self.menu_mode == "main":
            if pyxel.btnp(pyxel.KEY_X) or pyxel.btnp(pyxel.KEY_ESCAPE):
                if self.state == STATE_MENU:
                    # Determine where to return
                    # We can check current tile to see if we were in town
                    # But simpler is to check current state transition
                    pass
                u, v = pyxel.tilemaps[0].pget(self.px, self.py)
                self.state = STATE_FIELD if u != TILE_TOWN else STATE_TOWN
                return
            if pyxel.btnp(pyxel.KEY_UP): self.menu_cursor = (self.menu_cursor - 1) % 4
            elif pyxel.btnp(pyxel.KEY_DOWN): self.menu_cursor = (self.menu_cursor + 1) % 4
                
            if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN):
                if self.menu_cursor == 1: # Items
                    self.menu_mode = "items"
                    self.sub_cursor = 0
                elif self.menu_cursor == 2: # Magic
                    self.menu_mode = "magic_char"
                    self.sub_cursor = 0
                elif self.menu_cursor == 3: # Exit
                    u, v = pyxel.tilemaps[0].pget(self.px, self.py)
                    self.state = STATE_FIELD if u != TILE_TOWN else STATE_TOWN

                    
        elif self.menu_mode == "items":
            if pyxel.btnp(pyxel.KEY_X): self.menu_mode = "main"
            
            valid_items = [itm for itm in self.inventory if itm.amount > 0]
            if not valid_items: return
            
            if pyxel.btnp(pyxel.KEY_UP): self.sub_cursor = (self.sub_cursor - 1) % len(valid_items)
            elif pyxel.btnp(pyxel.KEY_DOWN): self.sub_cursor = (self.sub_cursor + 1) % len(valid_items)
            
            if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN):
                self.selected_item_or_spell = valid_items[self.sub_cursor]
                if self.selected_item_or_spell.effect_type in ["heal_hp", "heal_mp"]:
                    self.menu_mode = "target"
                    self.target_cursor = 0
                    
        elif self.menu_mode == "magic_char":
            if pyxel.btnp(pyxel.KEY_X): self.menu_mode = "main"
            if pyxel.btnp(pyxel.KEY_UP): self.sub_cursor = (self.sub_cursor - 1) % len(self.party)
            elif pyxel.btnp(pyxel.KEY_DOWN): self.sub_cursor = (self.sub_cursor + 1) % len(self.party)
            if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN):
                self.active_char = self.party[self.sub_cursor]
                if self.active_char and self.active_char.spells:
                    self.menu_mode = "magic"
                    self.sub_cursor = 0

        elif self.menu_mode == "magic":
            if pyxel.btnp(pyxel.KEY_X): self.menu_mode = "magic_char"
            if self.active_char and self.active_char.spells:
                if pyxel.btnp(pyxel.KEY_UP): self.sub_cursor = (self.sub_cursor - 1) % len(self.active_char.spells)
                elif pyxel.btnp(pyxel.KEY_DOWN): self.sub_cursor = (self.sub_cursor + 1) % len(self.active_char.spells)
                if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN):
                    spl = self.active_char.spells[self.sub_cursor]
                    if spl.effect_type == 'heal' and self.active_char.mp >= spl.mp_cost:
                        self.selected_item_or_spell = spl
                        self.menu_mode = "target"
                        self.target_cursor = 0

        elif self.menu_mode == "target":
            if pyxel.btnp(pyxel.KEY_X): self.menu_mode = "main"
            if pyxel.btnp(pyxel.KEY_UP): self.target_cursor = (self.target_cursor - 1) % len(self.party)
            elif pyxel.btnp(pyxel.KEY_DOWN): self.target_cursor = (self.target_cursor + 1) % len(self.party)
            
            if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN):
                target = self.party[self.target_cursor]
                eff = self.selected_item_or_spell
                if isinstance(eff, Item):
                    if eff.effect_type == "heal_hp":
                        target.hp = min(target.max_hp, target.hp + eff.power)
                    elif eff.effect_type == "heal_mp":
                        target.mp = min(target.max_mp, target.mp + eff.power)
                    eff.amount -= 1
                elif isinstance(eff, Spell) and self.active_char:
                    self.active_char.mp -= eff.mp_cost
                    target.hp = min(target.max_hp, target.hp + eff.power)
                self.menu_mode = "main"

    def push_command(self, char, action, target_info):
        self.character_commands.append((char, action, target_info))
        self.menu_mode = "main"
        self.battle_cursor = 0
        self.active_character_idx += 1
        if not self.get_next_alive_character():
            self.battle_phase = 2
            self.battle_messages.append("Turn starts!")
            self.execute_turn()

    def get_next_alive_character(self):
        while self.active_character_idx < len(self.party) and self.party[self.active_character_idx].hp <= 0:
            self.active_character_idx += 1
        return self.active_character_idx < len(self.party)

    def execute_turn(self):
        if not self.current_monster:
            return
            
        # Flee check
        for char, act, info in self.character_commands:
            if act == "Flee":
                self.battle_messages.append("Party fled!")
                self.battle_phase = 3
                return

        # Player actions
        for char, act, info in self.character_commands:
            if not self.current_monster or self.current_monster.hp <= 0: break
            if char.hp <= 0: continue
            
            if act == "Attack":
                dmg = max(1, char.attack - self.current_monster.defense // 2 + random.randint(-1, 1))
                self.current_monster.hp -= dmg
                self.battle_messages.append(f"{char.name} attacks! {dmg} dmg.")
            elif act == "Defend":
                self.battle_messages.append(f"{char.name} is defending.")
            elif act == "Magic":
                if isinstance(info, tuple): # Heal magic
                    spl, target = info
                    char.mp -= spl.mp_cost
                    target.hp = min(target.max_hp, target.hp + spl.power)
                    self.battle_messages.append(f"{char.name} cast {spl.name} on {target.name}!")
                else: # Attack magic
                    spl = info
                    char.mp -= spl.mp_cost
                    dmg = spl.power + random.randint(0, 5)
                    self.current_monster.hp -= dmg
                    self.battle_messages.append(f"{char.name} cast {spl.name}! {dmg} dmg.")
            elif act == "Item":
                itm, target = info
                if itm.amount > 0:
                    itm.amount -= 1
                    if itm.effect_type == "heal_hp":
                        target.hp = min(target.max_hp, target.hp + itm.power)
                    elif itm.effect_type == "heal_mp":
                        target.mp = min(target.max_mp, target.mp + itm.power)
                    self.battle_messages.append(f"Used {itm.name} on {target.name}.")

        # Monster attacks
        if self.current_monster and self.current_monster.hp > 0:
            alive = [c for c in self.party if c.hp > 0]
            if alive:
                target = random.choice(alive)
                # Reduced defense if defending
                def_mult = 1
                for c, a, i in self.character_commands:
                    if c == target and a == "Defend": def_mult = 2
                
                dmg = max(1, self.current_monster.attack - (target.defense*def_mult) // 2 + random.randint(-1, 1))
                target.hp -= dmg
                if target.hp < 0: target.hp = 0
                self.battle_messages.append(f"{self.current_monster.name} hits {target.name} for {dmg} dmg!")
                if target.hp == 0:
                    self.battle_messages.append(f"{target.name} fell!")
        elif self.current_monster:
            if self.is_boss_battle:
                self.battle_messages.append("The Demon Lord is defeated!")
                self.battle_messages.append("Peace returns to the world...")
                self.battle_phase = 3
                return

            self.battle_messages.append(f"Defeated {self.current_monster.name}!")
            self.battle_messages.append(f"Gained {self.current_monster.exp_yield} EXP!")
            lvl_up = False
            for c in self.party:
                if c.hp > 0:
                    c.exp += self.current_monster.exp_yield
                    if c.update_stats():
                        lvl_up = True
            if lvl_up: self.battle_messages.append("Someone leveled up!")
            self.party[0].gold += self.current_monster.gold_yield
            self.battle_phase = 3
            return

        # Check party wipe
        if all(c.hp == 0 for c in self.party):
            self.battle_messages.append("Party was wiped out...")
            self.px, self.py = 13, 4 # castle location
            self.party[0].gold //= 2
            for c in self.party:
                c.hp = c.max_hp // 2
            self.battle_phase = 3
            return
            
        self.battle_phase = 1
        self.active_character_idx = 0
        self.character_commands.clear()
        self.menu_mode = "main"

    def update_battle(self):
        if len(self.battle_messages) > 4:
            self.battle_messages = self.battle_messages[-4:]

        if self.battle_phase == 0:
            if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN):
                self.battle_phase = 1
                self.active_character_idx = 0
                self.get_next_alive_character()
                self.menu_mode = "main"
                self.battle_cursor = 0

        elif self.battle_phase == 1:
            char = self.party[self.active_character_idx]
            
            if self.menu_mode == "main":
                if pyxel.btnp(pyxel.KEY_UP): self.battle_cursor = (self.battle_cursor - 1) % 5
                elif pyxel.btnp(pyxel.KEY_DOWN): self.battle_cursor = (self.battle_cursor + 1) % 5
                
                if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN):
                    if self.battle_cursor == 0: # Attack
                        self.push_command(char, "Attack", None)
                    elif self.battle_cursor == 1: # Defend
                        self.push_command(char, "Defend", None)
                    elif self.battle_cursor == 2: # Magic
                        self.menu_mode = "magic"
                        self.sub_cursor = 0
                    elif self.battle_cursor == 3: # Item
                        self.menu_mode = "items"
                        self.sub_cursor = 0
                    elif self.battle_cursor == 4: # Flee
                        self.push_command(char, "Flee", None)
                        
                elif pyxel.btnp(pyxel.KEY_X):
                    if self.active_character_idx > 0:
                        self.active_character_idx -= 1
                        while self.party[self.active_character_idx].hp <= 0 and self.active_character_idx > 0:
                            self.active_character_idx -= 1
                        self.character_commands.pop()

            elif self.menu_mode == "magic":
                if pyxel.btnp(pyxel.KEY_X):
                    self.menu_mode = "main"
                    return # Xキーで確実に戻る
                if char.spells:
                    if pyxel.btnp(pyxel.KEY_UP): self.sub_cursor = (self.sub_cursor - 1) % len(char.spells)
                    elif pyxel.btnp(pyxel.KEY_DOWN): self.sub_cursor = (self.sub_cursor + 1) % len(char.spells)
                    if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN):
                        spl = char.spells[self.sub_cursor]
                        if char.mp >= spl.mp_cost:
                            if spl.effect_type == "damage":
                                self.push_command(char, "Magic", spl)
                            elif spl.effect_type == "heal":
                                self.selected_item_or_spell = spl
                                self.menu_mode = "target"
                                self.target_cursor = 0
            
            elif self.menu_mode == "items":
                if pyxel.btnp(pyxel.KEY_X):
                    self.menu_mode = "main"
                    return
                valid_items = [itm for itm in self.inventory if itm.amount > 0]
                if valid_items:
                    if pyxel.btnp(pyxel.KEY_UP): self.sub_cursor = (self.sub_cursor - 1) % len(valid_items)
                    elif pyxel.btnp(pyxel.KEY_DOWN): self.sub_cursor = (self.sub_cursor + 1) % len(valid_items)
                    if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN):
                        self.selected_item_or_spell = valid_items[self.sub_cursor]
                        self.menu_mode = "target"
                        self.target_cursor = 0

            elif self.menu_mode == "target":
                if pyxel.btnp(pyxel.KEY_X): self.menu_mode = "main"
                if pyxel.btnp(pyxel.KEY_UP): self.target_cursor = (self.target_cursor - 1) % len(self.party)
                elif pyxel.btnp(pyxel.KEY_DOWN): self.target_cursor = (self.target_cursor + 1) % len(self.party)
                if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN):
                    target = self.party[self.target_cursor]
                    self.push_command(char, "Item" if isinstance(self.selected_item_or_spell, Item) else "Magic", (self.selected_item_or_spell, target))

        elif self.battle_phase == 2:
            if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN):
                pass
                
        elif self.battle_phase == 3:
            if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN):
                if self.is_boss_battle:
                    self.state = STATE_GAMECLEAR
                    self.is_boss_battle = False
                else:
                    self.state = STATE_FIELD
                self.current_monster = None

    def draw_custom_title(self, x, y):
        # Draw "R..P...G" using custom 16x16 characters from image bank 1
        # Animation logic: show characters based on self.title_frame
        # Each step takes 15 frames
        # If any key is pressed during animation, show all characters
        if self.state != STATE_TITLE:
            step = 99
        else:
            step = self.title_frame // 15
        
        if step >= 1: pyxel.blt(x, y, 1, 0, 0, 16, 16, 0)      # R
        if step >= 2: pyxel.blt(x + 12, y, 1, 16, 0, 16, 16, 0) # .
        if step >= 3: pyxel.blt(x + 20, y, 1, 16, 0, 16, 16, 0) # .
        if step >= 4: pyxel.blt(x + 32, y, 1, 32, 0, 16, 16, 0) # P
        if step >= 5: pyxel.blt(x + 44, y, 1, 16, 0, 16, 16, 0) # .
        if step >= 6: pyxel.blt(x + 52, y, 1, 16, 0, 16, 16, 0) # .
        if step >= 7: pyxel.blt(x + 60, y, 1, 16, 0, 16, 16, 0) # .
        if step >= 8: pyxel.blt(x + 72, y, 1, 48, 0, 16, 16, 0) # G

    def draw(self):
        pyxel.cls(0)
        
        if self.state == STATE_TITLE:
            self.draw_custom_title(81, 100)
            # Only show start message after animation finishes (step 8+)
            if self.title_frame > 15 * 9:
                if (pyxel.frame_count // 15) % 2 == 0:
                    pyxel.text(85, 135, "Press ENTER to Start", 7)
        elif self.state == STATE_FIELD:
            self.draw_map(FIELD_MAP, MAP_WIDTH, MAP_HEIGHT, self.px, self.py)
            self.draw_objects("field")
            self.draw_party_status()
            if self.is_dialog_active: self.draw_dialog()
            self.draw_acquisition()
        elif self.state == STATE_TOWN:
            self.draw_map(TOWN_MAP, TOWN_WIDTH, TOWN_HEIGHT, self.tx, self.ty)
            self.draw_objects("town")
            self.draw_party_status()
            if self.is_dialog_active: self.draw_dialog()
            self.draw_acquisition()
        elif self.state == STATE_MENU:
            if self.is_town_mode():
                self.draw_map(TOWN_MAP, TOWN_WIDTH, TOWN_HEIGHT, self.tx, self.ty)
                self.draw_objects("town")
            else:
                self.draw_map(FIELD_MAP, MAP_WIDTH, MAP_HEIGHT, self.px, self.py)
                self.draw_objects("field")
            self.draw_field_menu()
            self.draw_acquisition()
        elif self.state == STATE_BATTLE:
            self.draw_battle()
        elif self.state == STATE_GAMECLEAR:
            pyxel.cls(0)
            pyxel.text(80, 80, "CONGRATULATIONS!", 10)
            pyxel.text(70, 100, "The Demon Lord is gone.", 7)
            pyxel.text(75, 120, "You are a True Hero!", 14)
            pyxel.text(85, 160, "Press ENTER to Title", 7)
            if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_Z):
                self.state = STATE_TITLE
                self.title_frame = 0 # Animation counter for title
                # Reset party
                self.party = [
                    Character("Yusha", 30, 0, 10, 5, 8),
                    Character("Saru", 25, 15, 7, 4, 10, [SPELL_FIRE]),
                    Character("Mimi", 18, 25, 4, 3, 12, [SPELL_HEAL])
                ]
                self.px, self.py = 20, 10

    def draw_acquisition(self):
        if self.acquisition_timer > 0:
            # Right top corner notification
            tw = len(self.acquisition_text) * 4 + 8
            pyxel.rect(pyxel.width - tw - 5, 5, tw, 12, 0)
            pyxel.rectb(pyxel.width - tw - 5, 5, tw, 12, 10)
            pyxel.text(pyxel.width - tw, 8, self.acquisition_text, 7)

    def draw_objects(self, mode):
        if mode == "field":
            for c in self.chests:
                tile = TILE_CHEST_CLOSED if not c.opened else TILE_CHEST_OPEN
                pyxel.blt(c.x*8-self.camera_x, c.y*8-self.camera_y, 0, tile*8, 0, 8, 8, 0)
        elif mode == "town":
            for n in self.npcs:
                pyxel.blt(n.x*8-self.camera_x, n.y*8-self.camera_y, 0, TILE_NPC*8, 0, 8, 8, 0)
            for c in self.town_chests:
                tile = TILE_CHEST_CLOSED if not c.opened else TILE_CHEST_OPEN
                pyxel.blt(c.x*8-self.camera_x, c.y*8-self.camera_y, 0, tile*8, 0, 8, 8, 0)


    def draw_dialog(self):
        # Dialog box at bottom
        pyxel.rect(10, 180, 236, 60, 0)
        pyxel.rectb(10, 180, 236, 60, 7)
        for i, msg in enumerate(self.dialog_text):
            pyxel.text(20, 190 + i*10, msg, 7)
        if pyxel.frame_count % 30 < 15:
            pyxel.text(200, 230, "[Z/ENTER]", 10)
        
        # Draw NPC portrait if available
        if self.active_npc:
            # Face box at top right
            pyxel.rect(210, 10, 36, 36, 0)
            pyxel.rectb(210, 10, 36, 36, 7)
            # Draw portrait from Bank 2 (each 32x32)
            # index is stored in active_npc.face_id
            u = (self.active_npc.face_id % 8) * 32
            v = (self.active_npc.face_id // 8) * 32
            pyxel.blt(212, 12, 2, u, v, 32, 32, 0)
            # Display Name
            pyxel.text(210, 48, self.active_npc.name, 10)

    def is_town_mode(self):
        # Determine if we are currently in town or field based on current tile
        u, v = pyxel.tilemaps[0].pget(self.px, self.py)
        return u == TILE_TOWN


    def draw_map(self, map_data, mw, mh, px, py):
        # FASTEST rendering using Pyxel's tilemap feature
        # We use tilemap 0 for world and 1 for town
        tm = 0 if (mw == MAP_WIDTH) else 1
        
        # bltm(x, y, tm, u, v, w, h, [colkey])
        pyxel.bltm(0, 0, tm, self.camera_x, self.camera_y, pyxel.width, pyxel.height, 0)
        
        # Draw player (Always use index 0 horizontally in Bank 0, Y=8)
        # Previously it was using self.facing * 8, which caused it to disappear when not facing down (0)
        pyxel.blt(px * 8 - self.camera_x, py * 8 - self.camera_y, 0, 0, 8, 8, 8, 0)

    def draw_party_status(self):
        # Move to bottom of the screen (y=232, height=24)
        pyxel.rect(0, 232, pyxel.width, 24, 0)
        pyxel.rectb(0, 232, pyxel.width, 24, 7)
        for i, char in enumerate(self.party):
            x = 4 + i * 80
            c = 7 if char.hp > 0 else 8
            pyxel.text(x, 236, f"Lv{char.level} {char.name[:4]}", c)
            pyxel.text(x, 244, f"H:{char.hp} M:{char.mp}", c)
            
            # Draw facing arrow for each character (or just the leader)
            # Displaying for each character at the bottom right of their status area
            if i == 0: # Show direction arrow for the party leader
                arrow = ["v", "^", "<", ">"][self.facing]
                pyxel.text(x + 50, 244, arrow, 10)
                
        # Display current Gold
        pyxel.text(205, 236, f"G:{self.party[0].gold}", 10)

    def draw_field_menu(self):
        pyxel.rect(170, 30, 80, 80, 0)
        pyxel.rectb(170, 30, 80, 80, 7)
        
        if self.menu_mode == "main":
            cmds = ["Status", "Items", "Magic", "Exit"]
            for i, c in enumerate(cmds):
                pyxel.text(185, 40 + i*15, c, 7)
            pyxel.text(175, 40 + self.menu_cursor*15, ">", 10)
            pyxel.text(175, 100, f"GOLD: {self.party[0].gold}", 10)
            
        elif self.menu_mode == "items":
            valid = [i for i in self.inventory if i.amount > 0]
            if not valid: pyxel.text(175, 40, "No Items", 7)
            for i, itm in enumerate(valid):
                pyxel.text(185, 40 + i*10, f"{itm.name} x{itm.amount}", 7)
            if valid: pyxel.text(175, 40 + self.sub_cursor*10, ">", 10)
            
        elif self.menu_mode == "magic_char":
            for i, c in enumerate(self.party):
                pyxel.text(185, 40 + i*10, c.name, 7)
            pyxel.text(175, 40 + self.sub_cursor*10, ">", 10)

        elif self.menu_mode == "magic":
            if self.active_char:
                for i, s in enumerate(self.active_char.spells):
                    pyxel.text(185, 40 + i*10, f"{s.name}({s.mp_cost})", 7)
                pyxel.text(175, 40 + self.sub_cursor*10, ">", 10)

        elif self.menu_mode == "target":
            for i, c in enumerate(self.party):
                col = 7 if c.hp > 0 else 8
                pyxel.text(185, 40 + i*10, f"{c.name} H:{c.hp}", col)
            pyxel.text(175, 40 + self.target_cursor*10, ">", 10)

    def draw_battle(self):
        pyxel.cls(0)
        if self.current_monster:
            # Determine monster tile based on name
            # All monsters now use 24x24 (bank 0, y=24) or 32x32 (bank 1, 64, 0)
            if self.current_monster.name == "DEMON LORD":
                # Boss uses 32x32 from Bank 1
                pyxel.blt(112, 70, 1, 64, 0, 32, 32, 0)
                # Display HP above the monster (y=60)
                pyxel.text(100, 60, f"{self.current_monster.name} HP:{self.current_monster.hp}", 8)
            else:
                # Regular monsters use 24x24 from Bank 0, Y=24
                idx = 0
                if self.current_monster.name == "Bat": idx = 1
                elif self.current_monster.name == "Goblin": idx = 2
                elif self.current_monster.name == "Scorpion": idx = 3
                elif self.current_monster.name == "Cactus": idx = 4
                elif self.current_monster.name == "FireSpirit": idx = 5
                elif self.current_monster.name == "LavaGolem": idx = 6
                elif self.current_monster.name == "RedDragon": idx = 7
                elif self.current_monster.name == "Yeti": idx = 8
                elif self.current_monster.name == "IceWolf": idx = 9
                elif self.current_monster.name == "SnowGhost": idx = 10
                
                pyxel.blt(116, 80, 0, idx * 24, 24, 24, 24, 0)
                # Display HP above the monster (y=70)
                pyxel.text(110, 70, f"{self.current_monster.name} HP:{self.current_monster.hp}", 8)


        pyxel.rect(0, 200, pyxel.width, 56, 0)
        pyxel.rectb(0, 200, pyxel.width, 56, 7)
        for i, char in enumerate(self.party):
            x = 8 + i * 80
            c = 7 if char.hp > 0 else 8
            if self.battle_phase == 1 and self.menu_mode == "main" and i == self.active_character_idx:
                pyxel.text(x-6, 208, ">", 10)
            pyxel.text(x, 208, char.name, c)
            pyxel.text(x, 218, f"HP:{char.hp}/{char.max_hp}", c)
            pyxel.text(x, 228, f"MP:{char.mp}/{char.max_mp}", 12)

        pyxel.rect(0, 0, pyxel.width, 50, 0)
        pyxel.rectb(0, 0, pyxel.width, 50, 7)
        for i, msg in enumerate(self.battle_messages):
            pyxel.text(4, 4 + i * 10, msg, 7)

        if self.battle_phase == 1:
            pyxel.rect(8, 130, 70, 65, 0)
            pyxel.rectb(8, 130, 70, 65, 7)
            
            if self.menu_mode == "main":
                cmds = ["Attack", "Defend", "Magic", "Item", "Flee"]
                for i, c in enumerate(cmds): pyxel.text(20, 135 + i*11, c, 7)
                pyxel.text(10, 135 + self.battle_cursor*11, ">", 10)
            elif self.menu_mode == "magic":
                char = self.party[self.active_character_idx]
                if not char.spells: pyxel.text(20, 135, "No Magic", 5)
                for i, s in enumerate(char.spells):
                    col = 7 if char.mp >= s.mp_cost else 5
                    pyxel.text(20, 135 + i*11, f"{s.name}({s.mp_cost})", col)
                if char.spells: pyxel.text(10, 135 + self.sub_cursor*11, ">", 10)
            elif self.menu_mode == "items":
                valid = [i for i in self.inventory if i.amount > 0]
                if not valid: pyxel.text(20, 135, "No Items", 5)
                for i, itm in enumerate(valid): pyxel.text(20, 135 + i*11, f"{itm.name}x{itm.amount}", 7)
                if valid: pyxel.text(10, 135 + self.sub_cursor*11, ">", 10)
            elif self.menu_mode == "target":
                for i, c in enumerate(self.party):
                    col = 7 if c.hp > 0 else 8
                    pyxel.text(20, 135 + i*11, c.name, col)
                pyxel.text(10, 135 + self.target_cursor*11, ">", 10)

        elif self.battle_phase in (2, 3) and pyxel.frame_count % 30 < 15:
            pyxel.text(200, 40, "[Z] Next", 10)

App()
