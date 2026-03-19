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
TILE_SIZE = 8 # Reverted to 8 for stability, but we can still draw 32x32 sprites on it
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
TILE_BOSS = 15
TILE_CAVE = 16 # New Cave Tile

# Map Data - Redesigned Land-based World Map (No Sea)
# 0:Grass, 1:Forest, 2:Mountain, 3:Water(Removed), 4:Castle, 5:Town, 8:Bridge, 9:Sand, L:Lava, S:Snow, B:Boss, C:Cave
FIELD_MAP = [
    "2222222222222222222222222222222222222222222222222222222222222222",
    "2SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS2",
    "2SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS2",
    "2SSSSSS22222222SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS2",
    "2SSSSSS2SSSSSS22SSSSSSSSSSSSS222222SSSSSSSSSSSSSSSSSSSSSSSSSSSS2",
    "2SSSSSS2SS5SSS122SSSSSSSSSSS22111122SSSSSSSSSSSSSSSSSSSSSSSSSSS2",
    "2SSSSSS2SSSSSS1122SSSSSSSSS2211111122SSSSSSSSSSSSSSSSSSSSSSSSSS2",
    "2SSSSSS222222211122SSSSSSS221111111122SSSSSSSSSSSSSSSSSSSSSSSSS2",
    "2SSSSSSSSS1111111122SSSSS22111111111122SSSSSSSSSSSSSSSSSSSSSSSS2",
    "2SSSSSSSSSS1111111122SSS2211111111111122SSSSSSSSSSSSSSSSSSSSSSS2",
    "22222222222221111111122S2211111111111111222222222222222222222222",
    "2222222222222211111111122221111111111111112222222222222222222222",
    "2222222222221111111111112211111111111111111122222222222222222222",
    "2222222222211111111111111111111111111111111112222222222222222222",
    "2222222222111111111111111111111111111111111111222222222222222222",
    "2222222221111111111111111111111111111111111111122222222222222222",
    "2222222211111111111111000000001111111111111111112222222222222222",
    "2222222111111111111110000000000111111111111111111222222222222222",
    "2222221111111111111100000000000011111111111111111122222222222222",
    "2222211111111111111100000011110001111111111111111122222222222222",
    "2222111111111111111000011111111000111111111111111112222222222222",
    "2221111111111111111000011111111000111111111111111111222222222222",
    "2221111111111111111000000011110000111111111111111111122222222222",
    "2211111111111111111000000000000001111111111111111111112222222222",
    "2211111111111111111100000000000011111111111111111111111222222222",
    "2211111111111111111110000000000111111111111111111111111222222222",
    "2221111111111111111111111111111111111111111111111111112222222222",
    "2222111111111111111111111111111111111111111111111111122222222222",
    "2222211111111111111111111111111111111111111111111111222222222222",
    "2222221111111111111111111111111111111111111111111112222222222222",
    "2222222211111111111111111111111111111111111111111222222222222222",
    "2222222222111111111111111111111111111111111111222222222222222222",
    "2222222222222111111111111111111111111111111222222222222222222222",
    "2222222222222222211111111111111111111111222222222222222222222222",
    "2222222222222222222221111111111112222222222222222222222222222222",
    "2222222222222222222222200000000222222222222222222222222222222222",
    "2222222222222222222222220011110022222222222222222222222222222222",
    "2222222222222222222222220011110022222222222222222222222222222222",
    "2222222222222222222222220011110022222222222222222222222222222222",
    "2222222222222222222222220011110022222222222222222222222222222222",
    "2222222222222222222222220011110022222222222222222222222222222222",
    "2222222222222222222222220011110022222222222222222222222222222222",
    "2222222222222222222222220011110022222222222222222222222222222222",
    "2222222222222222222222220011110022222222222222222222222222222222",
    "2222222222222222222222220011110022222222222222222222222222222222",
    "2222222222222222222222220011110022222222222222222222222222222222",
    "2222222222222222222222220011110022222222222222222222222222222222",
    "2222222222222222222222220011110022222222222222222222222222222222",
    "2222222222222222222222220011110022222222222222222222222222222222",
    "2222222222222222222222220011110022222222222222222222222222222222",
    "2222222222222222222222220011110022222222222222222222222222222222",
    "2222222222222222222222220011110022222222222222222222222222222222",
    "2222222222222222222222220011110022222222222222222222222222222222",
    "2222222222222222222222220011110022222222222222222222222222222222",
    "2222221111111111111111110011110011111111111111110011110022222222",
    "2222299999992222222222220011110022222222222222220011110022222222",
    "22229999119992222222222200111100222222222222222LLLLLL22222222222",
    "2222999915199922222222220011110022222222222222LLLLLLL22222222222",
    "222299991199922222222222001111002222222222222LLLLLLLL22222222222",
    "22222999999922222222222222000022222222222222LLLL4LLL222222222222",
    "22222299999222222222222222222222222222222222LLLLLLL222222222222",
    "222222222222222222222222222222222222222222222LLLLLC222222222222",
    "2222222222222222222222222222222222222222222222222222222222222222",
    "2222222222222222222222222222222222222222222222222222222222222222",
    "2222222222222222222222222222222222222222222222211111111112222222",
    "222222222222222222222222222222222222222222222221LLLLLC2222222222",
    "222222222222222222222222222222222222222222222221LLLLLL2222222222",
]

MAP_WIDTH = len(FIELD_MAP[0])
MAP_HEIGHT = len(FIELD_MAP)

# Town Map Data (Expanded to 32x32 for Full Screen 256x256)
# 0:Grass, 6:Floor, 7:Wall
TOWN_MAP = [
    "77777777777777777777777777777777",
    "76666666666666666666666666666667",
    "76666666666666666666666666666667",
    "76667777766666666666667777766667",
    "76667666766666666666667666766667",
    "76667666766666666666667666766667",
    "76667767766666666666667767766667",
    "76666666666666666666666666666667",
    "76666666666666666666666666666667",
    "76666666666677777666666666666667",
    "76666666666676667666666666666667",
    "76666666666676667666666666666667",
    "76666666666677677666666666666667",
    "76666666666666666666666666666667",
    "76666666666666666666666666666667",
    "77777776677777777777777667777777",
    "00000076670000000000007667000000",
    "00000076670000000000007667000000",
    "00000076670000000000007667000000",
    "00000076677777777777777667000000",
    "00000076666666666666666667000000",
    "00000076666666666666666667000000",
    "00000077777777766777777777000000",
    "00000000000000766700000000000000",
    "00000000000000766700000000000000",
    "00000000000000766700000000000000",
    "00000000000000766700000000000000",
    "00000000000000766700000000000000",
    "00000000000000766700000000000000",
    "00000000000000766700000000000000",
    "00000000000000766700000000000000",
    "00000000000000766700000000000000",
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
    def __init__(self, name, hp, attack, defense, exp_yield, gold_yield, img_file=None):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.exp_yield = exp_yield
        self.gold_yield = gold_yield
        self.img_file = img_file

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
        self.facing = 0 # 0: down, 1: up, 2: left, 3: right

    def update(self, app):
        if not self.is_moving:
            return

        self.move_timer += 1
        if self.move_timer > 30: # Move every 30 frames
            self.move_timer = 0
            dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)])
            nx, ny = self.x + dx, self.y + dy
            
            # Update facing based on move
            if dx == 0 and dy == 1: self.facing = 0
            elif dx == 0 and dy == -1: self.facing = 1
            elif dx == -1 and dy == 0: self.facing = 2
            elif dx == 1 and dy == 0: self.facing = 3
            
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
        self.tx = 15
        self.ty = 30
        
        self.facing = 0 # 0: down, 1: up, 2: left, 3: right
        
        self.party = [
            Character("Zany(Hero)", 30, 0, 10, 5, 8),
            Character("Kozu(Mage)", 25, 15, 7, 4, 10, [SPELL_FIRE]),
            Character("Luna(Priest)", 18, 25, 4, 3, 12, [SPELL_HEAL])
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
             Chest(2, 2, Item("Herb", "heal_hp", 30, 1)), # Town corner
             Chest(29, 2, Item("MagicWater", "heal_mp", 15, 1)), # Another corner
        ]

        self.npcs = [
            NPC(15, 20, "Villager", ["Welcome to our large town!", "The desert island to the SW is hot,", "but the lava island to the SE is DEADLY!"], True, 0),
            NPC(8, 5, "Elder", ["To defeat the Demon Lord in the lava region,", "you must train well in the snow mountains."], False, 1),
            NPC(25, 5, "Guard", ["The castle is to the north.", "Rest there to recover your HP and MP."], False, 2),
            NPC(14, 11, "Girl", ["I love the white snow in the north!", "Have you seen the Snow Ghost?"], True, 3),
            NPC(15, 25, "Merchant", ["I have no items to sell right now...", "But you can find treasures in the islands!"], False, 0)
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
        
        self.shake_amount = 0
        self.flash_timer = 0
        
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
        # 0: Grass (Lush with small flower dots)
        pyxel.images[0].rect(0, 0, 8, 8, 3) 
        pyxel.images[0].pset(1, 1, 11); pyxel.images[0].pset(5, 4, 11)
        pyxel.images[0].pset(2, 6, 14) # A tiny pink flower dot
        
        # 1: Forest (Layered trees)
        pyxel.images[0].rect(8, 0, 8, 8, 3)
        pyxel.images[0].circ(11, 3, 3, 11)
        pyxel.images[0].circ(11, 5, 2, 3)
        pyxel.images[0].line(11, 5, 11, 7, 4) # Trunk
        
        # 2: Mountain (Rocky cliff/crag style)
        pyxel.images[0].rect(16, 0, 8, 8, 4) # Dark Brown/Grey base
        # Draw some irregular rocky shapes
        pyxel.images[0].line(16, 2, 19, 0, 13); pyxel.images[0].line(19, 0, 23, 4, 13) # Jagged top
        pyxel.images[0].line(16, 5, 20, 3, 13); pyxel.images[0].line(20, 3, 23, 7, 13) # Middle crack
        pyxel.images[0].pset(18, 2, 7); pyxel.images[0].pset(21, 5, 7) # Highlights
        pyxel.images[0].line(16, 7, 23, 7, 0) # Bottom shadow
        
        # 3: Water (Animated-style waves)
        pyxel.images[0].rect(24, 0, 8, 8, 1)
        pyxel.images[0].line(24, 2, 26, 2, 12); pyxel.images[0].line(28, 5, 30, 5, 12)
        
        # 4: Castle (Stone walls and blue roof)
        pyxel.images[0].rect(32, 0, 8, 8, 3)
        pyxel.images[0].rect(33, 2, 6, 6, 13) # Stone base
        pyxel.images[0].rect(34, 4, 4, 4, 7)  # Gate area
        pyxel.images[0].tri(32, 2, 36, 0, 40, 2, 12) # Blue Roof
        
        # 5: Town (Quaint cottage style)
        pyxel.images[0].rect(40, 0, 8, 8, 3)
        pyxel.images[0].rect(41, 4, 6, 4, 15) # White walls
        pyxel.images[0].tri(40, 4, 44, 1, 48, 4, 8)  # Red Roof
        pyxel.images[0].rect(43, 6, 2, 2, 4)  # Small door
        
        # 6: Town Floor (Clean simple floor for character visibility)
        # Using Color 9 (Light Brown/Beige) - Good contrast for both Red(8) and Blue(12)
        pyxel.images[0].rect(48, 0, 8, 8, 9) 
        pyxel.images[0].pset(48, 0, 4); pyxel.images[0].pset(55, 7, 4) # Minimal corner dots

        
        # 7: Town Wall (Bricks)
        pyxel.images[0].rect(56, 0, 8, 8, 4)
        pyxel.images[0].line(56, 3, 63, 3, 0); pyxel.images[0].line(56, 7, 63, 7, 0)
        pyxel.images[0].line(59, 0, 59, 3, 0); pyxel.images[0].line(61, 4, 61, 7, 0)
        
        # 8: Bridge (Wooden planks)
        pyxel.images[0].rect(64, 0, 8, 8, 4) # Dark wood base
        pyxel.images[0].rect(64, 1, 8, 6, 9) # Lighter wood
        for i in range(65, 72, 2): pyxel.images[0].line(i, 1, i, 6, 4)
        
        # 9: Sand (Dunes with shadows)
        pyxel.images[0].rect(72, 0, 8, 8, 10)
        pyxel.images[0].line(72, 3, 75, 5, 9); pyxel.images[0].line(76, 2, 79, 4, 9)
        
        # 10: Lava (Glowing with bubbles)
        pyxel.images[0].rect(80, 0, 8, 8, 8)
        pyxel.images[0].circ(82, 3, 1, 10); pyxel.images[0].circ(85, 6, 1, 2)
        
        # 11: Snow (Sparkling white)
        pyxel.images[0].rect(88, 0, 8, 8, 7)
        pyxel.images[0].pset(89, 2, 15); pyxel.images[0].pset(93, 6, 15)
        pyxel.images[0].pset(91, 4, 13)

        # 16: Cave (Dark entrance)
        pyxel.images[0].rect(128, 0, 8, 8, 4) # Mountain-like base
        pyxel.images[0].rect(130, 3, 4, 5, 0) # Dark hole
        pyxel.images[0].circ(132, 3, 2, 0)    # Rounded top of hole
        # 12: Treasure Chest (Closed)
        pyxel.images[0].rect(96, 0, 8, 8, 0)
        pyxel.images[0].rect(97, 2, 6, 5, 9) # Brown box
        pyxel.images[0].rect(97, 2, 6, 2, 4) # Lid top
        pyxel.images[0].pset(100, 4, 10) # Yellow lock
        # 13: Treasure Chest (Open)
        pyxel.images[0].rect(104, 0, 8, 8, 0)
        pyxel.images[0].rect(105, 4, 6, 3, 9)
        # 14: NPC (Original Simple Style)
        pyxel.images[0].rect(112, 0, 8, 8, 0)
        pyxel.images[0].rect(114, 1, 4, 3, 15) # Face
        pyxel.images[0].rect(114, 4, 4, 4, 12) # Blue body
        
        # Player Graphics (8x8) - 4 Directions in Bank 0, Y=8
        
        # 0: Down (Front) - Two blue eyes centered (shifted 1px left as requested)
        pyxel.images[0].rect(0, 8, 8, 8, 0)
        pyxel.images[0].rect(2, 9, 4, 3, 15) # Face (White)
        pyxel.images[0].rect(2, 12, 4, 4, 8)  # Body (Red)
        pyxel.images[0].pset(2, 10, 12); pyxel.images[0].pset(4, 10, 12) # Two blue eyes
        
        # 1: Up (Back) - No eyes
        pyxel.images[0].rect(8, 8, 8, 8, 0)
        pyxel.images[0].rect(10, 9, 4, 3, 15) # Head (White)
        pyxel.images[0].rect(10, 12, 4, 4, 8) # Body (Red)
        # Clear any eyes (pset color 15)
        pyxel.images[0].pset(10, 10, 15); pyxel.images[0].pset(12, 10, 15)
        
        # 2: Left (Side) - One blue eye (left)
        pyxel.images[0].rect(16, 8, 8, 8, 0)
        pyxel.images[0].rect(18, 9, 4, 3, 15) # Face
        pyxel.images[0].rect(18, 12, 4, 4, 8) # Body
        pyxel.images[0].pset(18, 10, 12) # Leading blue eye
        
        # 3: Right (Side) - One blue eye (right)
        pyxel.images[0].rect(24, 8, 8, 8, 0)
        pyxel.images[0].rect(26, 9, 4, 3, 15) # Face
        pyxel.images[0].rect(26, 12, 4, 4, 8) # Body
        pyxel.images[0].pset(29, 10, 12) # Leading blue eye

        # NPC Graphics (8x8) - 4 Directions in Bank 0, Y=40 (Moved again to be safe)
        # Body Color: Blue=12, Face Color: White=15 (Head stays white)
        
        # 0: Down (Front) - Two blue eyes
        pyxel.images[0].rect(0, 40, 8, 8, 0)
        pyxel.images[0].rect(2, 41, 4, 3, 15) # Head (White)
        pyxel.images[0].rect(2, 44, 4, 4, 12) # Body (Blue)
        pyxel.images[0].pset(2, 42, 12); pyxel.images[0].pset(4, 42, 12) # Two blue eyes
        
        # 1: Up (Back) - No eyes
        pyxel.images[0].rect(8, 40, 8, 8, 0)
        pyxel.images[0].rect(10, 41, 4, 3, 15) # Head (White)
        pyxel.images[0].rect(10, 44, 4, 4, 12) # Body (Blue)
        # FORCE CLEAR any eyes
        pyxel.images[0].pset(10, 42, 15); pyxel.images[0].pset(12, 42, 15)
        
        # 2: Left (Side) - One blue eye (left edge)
        pyxel.images[0].rect(16, 40, 8, 8, 0)
        pyxel.images[0].rect(18, 41, 4, 3, 15) # Face (White)
        pyxel.images[0].rect(18, 44, 4, 4, 12) # Body (Blue)
        pyxel.images[0].pset(18, 42, 12) # Leading eye
        
        # 3: Right (Side) - One blue eye (right edge)
        pyxel.images[0].rect(24, 40, 8, 8, 0)
        pyxel.images[0].rect(26, 41, 4, 3, 15) # Face (White)
        pyxel.images[0].rect(26, 44, 4, 4, 12) # Body (Blue)
        pyxel.images[0].pset(29, 42, 12) # Leading eye
        
        # Monsters (Start at Y=16 in Image Bank 0) - DEFINING AT Y=16 TO AVOID OVERLAP
        # Slime (0, 16)
        pyxel.images[0].rect(0, 16, 16, 16, 0)
        pyxel.images[0].circ(8, 28, 5, 12); pyxel.images[0].rect(3, 28, 10, 4, 12)
        pyxel.images[0].pset(6, 27, 7); pyxel.images[0].pset(10, 27, 7)
        # Bat (16, 16)
        pyxel.images[0].rect(16, 16, 16, 16, 0)
        pyxel.images[0].circ(24, 24, 3, 13)
        pyxel.images[0].line(18, 20, 24, 24, 5); pyxel.images[0].line(30, 20, 24, 24, 5)
        # Goblin (32, 16)
        pyxel.images[0].rect(32, 16, 16, 16, 0)
        pyxel.images[0].circ(40, 22, 4, 3); pyxel.images[0].rect(38, 26, 4, 6, 3)
        pyxel.images[0].pset(38, 21, 10); pyxel.images[0].pset(42, 21, 10)
        # Scorpion (48, 16)
        pyxel.images[0].rect(48, 16, 16, 16, 0)
        pyxel.images[0].rect(52, 26, 8, 4, 9)
        pyxel.images[0].line(56, 26, 56, 18, 9); pyxel.images[0].pset(58, 18, 8)
        # Cactus (64, 16)
        pyxel.images[0].rect(64, 16, 16, 16, 0)
        pyxel.images[0].rect(70, 20, 4, 12, 3)
        pyxel.images[0].rect(66, 24, 4, 2, 3); pyxel.images[0].rect(74, 22, 4, 2, 3)
        # FireSpirit (80, 16)
        pyxel.images[0].rect(80, 16, 16, 16, 0)
        pyxel.images[0].circ(88, 26, 4, 8); pyxel.images[0].tri(84, 26, 88, 18, 92, 26, 10)
        # LavaGolem (96, 16)
        pyxel.images[0].rect(96, 16, 16, 16, 0)
        pyxel.images[0].rect(100, 20, 8, 8, 2); pyxel.images[0].rect(102, 22, 4, 4, 8)
        # RedDragon (112, 16)
        pyxel.images[0].rect(112, 16, 16, 16, 0)
        pyxel.images[0].rect(116, 24, 8, 6, 8); pyxel.images[0].tri(112, 20, 116, 24, 112, 28, 8)
        # Yeti (128, 16)
        pyxel.images[0].rect(128, 16, 16, 16, 0)
        pyxel.images[0].circ(136, 24, 6, 7); pyxel.images[0].pset(134, 23, 0); pyxel.images[0].pset(138, 23, 0)
        # IceWolf (144, 16)
        pyxel.images[0].rect(144, 16, 16, 16, 0)
        pyxel.images[0].rect(148, 24, 8, 6, 12); pyxel.images[0].tri(154, 24, 158, 20, 158, 28, 12)
        # SnowGhost (160, 16)
        pyxel.images[0].rect(160, 16, 16, 16, 0)
        pyxel.images[0].circ(168, 24, 5, 13); pyxel.images[0].pset(166, 22, 12); pyxel.images[0].pset(170, 22, 12)

        # DEMON LORD (Bank 1, 64, 0)
        pyxel.images[1].rect(64, 0, 32, 32, 0)
        pyxel.images[1].rect(70, 10, 20, 20, 2)
        pyxel.images[1].tri(64, 0, 75, 15, 64, 32, 8)
        pyxel.images[1].tri(96, 0, 85, 15, 96, 32, 8)
        pyxel.images[1].rect(76, 15, 3, 3, 10); pyxel.images[1].rect(82, 15, 3, 3, 10)
        pyxel.images[1].rect(78, 22, 5, 2, 8)




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

        # Sound Effects (SFX)
        # 0: Walk
        pyxel.sounds[0].set("a1", "p", "7", "v", 3)
        # 1: Confirm/Select
        pyxel.sounds[1].set("c3", "p", "7", "n", 5)
        # 2: Hit
        pyxel.sounds[2].set("c1", "n", "7", "v", 8)
        # 3: Magic
        pyxel.sounds[3].set("e3g3c4", "s", "7", "v", 15)
        # 4: Treasure
        pyxel.sounds[4].set("c3e3g3c4", "p", "7", "v", 20)

    def is_passable(self, tx, ty, m_type="field"):
        if m_type == "field":
            if tx < 0 or tx >= MAP_WIDTH or ty < 0 or ty >= MAP_HEIGHT: return False
            # Get tile from Tilemap 0
            u, v = pyxel.tilemaps[0].pget(tx, ty)
            return u not in (TILE_MOUNTAIN, TILE_WATER) or u == TILE_BRIDGE or u == TILE_BOSS
        elif m_type == "town":
            if tx < 0 or tx >= TOWN_WIDTH or ty < 0 or ty >= TOWN_HEIGHT: return False
            u, v = pyxel.tilemaps[1].pget(tx, ty)
            return u != TILE_WALL

    def start_boss_battle(self):
        self.current_monster = Monster("DEMON LORD", 500, 40, 30, 0, 0, "IMG_4318.PNG")
        self.is_boss_battle = True
        self.state = STATE_BATTLE
        self.battle_phase = 0
        self.battle_messages = ["The ground shakes...", "DEMON LORD appears!"]
        self.character_commands = []
        self.active_character_idx = 0
        self.menu_mode = "main"
        self.battle_cursor = 0
        self.load_monster_image(self.current_monster)

    def trigger_random_encounter(self):
        # Get current tile from Tilemap 0
        u, v = pyxel.tilemaps[0].pget(self.px, self.py)
        tile = u
        
        if random.random() < 0.05:
            monsters = [
                Monster("Slime", 15, 7, 2, 5, 10, "IMG_4317.PNG"),
                Monster("Bat", 18, 9, 3, 8, 15, "IMG_4319.PNG"),
                Monster("Goblin", 25, 12, 5, 12, 25, "IMG_4320.PNG")
            ]
            
            # Area specific monsters
            if tile == TILE_SAND:
                monsters.append(Monster("Scorpion", 30, 15, 8, 20, 40, "IMG_4321.PNG"))
                monsters.append(Monster("Cactus", 20, 10, 15, 15, 30, "IMG_4323.PNG"))
            elif tile == TILE_LAVA:
                monsters = [
                    Monster("FireSpirit", 40, 18, 10, 30, 50, "IMG_4325.PNG"),
                    Monster("LavaGolem", 60, 22, 20, 50, 100, "IMG_4326.PNG"),
                    Monster("RedDragon", 100, 30, 25, 200, 500, "IMG_4327.PNG")
                ]
            elif tile == TILE_SNOW:
                monsters = [
                    Monster("Yeti", 45, 20, 12, 40, 60, "IMG_4328.PNG"),
                    Monster("IceWolf", 35, 15, 8, 25, 35, "IMG_4329.PNG"),
                    Monster("SnowGhost", 25, 12, 30, 35, 45, "IMG_4330.PNG")
                ]

            self.current_monster = random.choice(monsters)
            self.state = STATE_BATTLE
            self.battle_phase = 0
            self.battle_messages = [f"A wild {self.current_monster.name} appeared!"]
            self.character_commands = []
            self.active_character_idx = 0
            self.menu_mode = "main"
            self.battle_cursor = 0
            self.load_monster_image(self.current_monster)

    def load_monster_image(self, monster):
        if not monster or not monster.img_file:
            return
        import os
        base_path = os.path.dirname(__file__)
        img_path = os.path.join(base_path, "img32", monster.img_file)
        try:
            if os.path.exists(img_path):
                # Load the monster image into Bank 1 at (160, 0)
                # This leaves space for the player at (128, 0)
                pyxel.images[1].load(160, 0, img_path)
                # DEBUG: Print success
                # print(f"Loaded monster image: {img_path}")
            else:
                print(f"Warning: {img_path} not found.")
        except Exception as e:
            print(f"Warning: Could not load {monster.img_file}: {e}")

    def play_bgm(self, file_name):
        import os
        base_path = os.path.dirname(__file__)
        # Search in multiple potential locations
        paths = [
            os.path.join(base_path, "BGM", file_name),
            os.path.join(os.path.dirname(base_path), "noteuse", "BGM", file_name)
        ]
        for path in paths:
            try:
                if os.path.exists(path):
                    # Pyxel 2.0+ supports PCM playback for .mp3/.wav
                    # Sound channel 63 is often used for this in Pyxel
                    pyxel.sounds[63].pcm(path)
                    pyxel.play(0, 63, loop=True)
                    return
            except Exception as e:
                print(f"Failed to play BGM {file_name} from {path}: {e}")

    def update(self):
        # Update BGM on state change
        if not hasattr(self, 'last_state'):
            self.last_state = None
        
        if self.state != self.last_state:
            if self.state == STATE_TITLE:
                self.play_bgm("ComfyUI_00001_.mp3")
            elif self.state in [STATE_FIELD, STATE_TOWN]:
                self.play_bgm("ComfyUI_00002_.mp3")
            elif self.state == STATE_BATTLE:
                self.play_bgm("ComfyUI_00003_.mp3")
            elif self.state == STATE_GAMECLEAR:
                self.play_bgm("ComfyUI_00004_.mp3")
            self.last_state = self.state

        # Update acquisition timer
        if self.acquisition_timer > 0:
            self.acquisition_timer -= 1

        if self.state == STATE_TITLE:
            self.title_frame += 1
            # Check for Enter, Z key, or any gamepad button/input to start
            if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
                pyxel.play(3, 1)
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
            
        if self.shake_amount > 0:
            self.shake_amount -= 1
        if self.flash_timer > 0:
            self.flash_timer -= 1


    def update_field(self):
        if self.is_dialog_active:
            if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
                self.is_dialog_active = False
            return

        if pyxel.btnp(pyxel.KEY_X) or pyxel.btnp(pyxel.KEY_ESCAPE) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B):
            self.state = STATE_MENU
            self.menu_mode = "main"
            self.menu_cursor = 0
            return

        moved = False
        nx, ny = self.px, self.py

        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP): 
            ny -= 1
            self.facing = 1
            moved = True
        elif pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN): 
            ny += 1
            self.facing = 0
            moved = True
        elif pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT): 
            nx -= 1
            self.facing = 2
            moved = True
        elif pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT): 
            nx += 1
            self.facing = 3
            moved = True

        if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
            # Interact with objects in front of the player
            ix, iy = self.px, self.py
            if self.facing == 0: iy += 1
            elif self.facing == 1: iy -= 1
            elif self.facing == 2: ix -= 1
            elif self.facing == 3: ix += 1
            
            for c in self.chests:
                if c.x == ix and c.y == iy and not c.opened:
                    c.opened = True
                    pyxel.play(3, 4)
                    if c.item:
                        self.add_item(Item(c.item.name, c.item.effect_type, c.item.power, c.item.amount))
                        self.show_dialog([f"Found {c.item.name}!"])
                    else:
                        self.party[0].gold += c.gold
                        self.show_acquisition(f"GET: {c.gold} GOLD")
                        self.show_dialog([f"Found {c.gold} GOLD!"])
                    return

        # Movement with 32x32 TILE_SIZE logic
        if moved and pyxel.frame_count % 4 == 0:
            pyxel.play(3, 0)
            if self.is_passable(nx, ny, "field"):
                # Check collision with chests on field
                chest_blocked = False
                for c in self.chests:
                    if c.x == nx and c.y == ny:
                        chest_blocked = True
                        break
                
                if not chest_blocked:
                    self.px, self.py = nx, ny
                    
                    u, v = pyxel.tilemaps[0].pget(self.px, self.py)
                    tile = u
                    if tile == TILE_LAVA:
                        for c in self.party:
                            if c.hp > 0:
                                c.hp = max(1, c.hp - 1)
                    
                    if tile == TILE_BOSS:
                        self.start_boss_battle()
                        return

                    if tile == TILE_CAVE:
                        # Cave Warp Logic
                        # Cave A (Mainland): (53, 97) -> Cave B (Boss Island): (53, 101)
                        if self.px == 53 and self.py == 97:
                            self.px, self.py = 53, 101
                            self.show_dialog(["Traversed the dark cave..."])
                        elif self.px == 53 and self.py == 101:
                            self.px, self.py = 53, 97
                            self.show_dialog(["Returned to the mainland."])
                        return

                    if tile == TILE_CASTLE:
                        for c in self.party:
                            c.hp = c.max_hp
                            c.mp = c.max_mp
                    elif tile == TILE_TOWN:
                        self.save_px, self.save_py = self.px, self.py
                        self.state = STATE_TOWN
                        self.tx = 7
                        self.ty = 14
                    else:
                        self.trigger_random_encounter()

        # Camera centered on 8x8 tiles
        self.camera_x = self.px * 8 - pyxel.width // 2
        self.camera_y = self.py * 8 - pyxel.height // 2


    def update_town(self):
        if self.is_dialog_active:
            if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
                self.is_dialog_active = False
            return

        for n in self.npcs:
            n.update(self)

        if pyxel.btnp(pyxel.KEY_X) or pyxel.btnp(pyxel.KEY_ESCAPE) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B):
            self.state = STATE_MENU
            self.menu_mode = "main"
            self.menu_cursor = 0
            return
            
        nx, ny = self.tx, self.ty
        moved = False
        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP): 
            ny -= 1
            self.facing = 1
            moved = True
        elif pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN): 
            ny += 1
            self.facing = 0
            moved = True
        elif pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT): 
            nx -= 1
            self.facing = 2
            moved = True
        elif pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT): 
            nx += 1
            self.facing = 3
            moved = True

        if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
            ix1, iy1 = self.tx, self.ty
            ix2, iy2 = self.tx, self.ty
            if self.facing == 0: iy1 += 1; iy2 += 2
            elif self.facing == 1: iy1 -= 1; iy2 -= 2
            elif self.facing == 2: ix1 -= 1; ix2 -= 2
            elif self.facing == 3: ix1 += 1; ix2 += 2
            
            for n in self.npcs:
                if (n.x == ix1 and n.y == iy1) or (n.x == ix2 and n.y == iy2):
                    self.show_dialog(n.messages, n)
                    return
            
            for c in self.town_chests:
                if c.x == ix1 and c.y == iy1 and not c.opened:
                    c.opened = True
                    pyxel.play(3, 4)
                    if c.item:
                        self.add_item(Item(c.item.name, c.item.effect_type, c.item.power, c.item.amount))
                        self.show_dialog([f"Found {c.item.name}!"])
                    else:
                        self.party[0].gold += c.gold
                        self.show_acquisition(f"GET: {c.gold} GOLD")
                        self.show_dialog([f"Found {c.gold} GOLD!"])
                    return

        if moved and pyxel.frame_count % 3 == 0:
            pyxel.play(3, 0)
            if ny >= TOWN_HEIGHT:
                self.state = STATE_FIELD
                self.px, self.py = self.save_px, self.save_py
                if self.is_passable(self.px, self.py+1, "field"): self.py += 1
                return

            if (nx != self.tx or ny != self.ty) and self.is_passable(nx, ny, "town"):
                occupied = False
                for n in self.npcs:
                    if n.x == nx and n.y == ny: occupied = True; break
                for c in self.town_chests:
                    if c.x == nx and c.y == ny: occupied = True; break
                if not occupied:
                    self.tx, self.ty = nx, ny

        # Camera centered on 8x8 tiles
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
            if pyxel.btnp(pyxel.KEY_X) or pyxel.btnp(pyxel.KEY_ESCAPE) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B):
                u, v = pyxel.tilemaps[0].pget(self.px, self.py)
                self.state = STATE_FIELD if u != TILE_TOWN else STATE_TOWN
                return
            if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP): self.menu_cursor = (self.menu_cursor - 1) % 4
            elif pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN): self.menu_cursor = (self.menu_cursor + 1) % 4
                
            if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
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
            if pyxel.btnp(pyxel.KEY_X) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B): self.menu_mode = "main"
            
            valid_items = [itm for itm in self.inventory if itm.amount > 0]
            if not valid_items: return
            
            if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP): self.sub_cursor = (self.sub_cursor - 1) % len(valid_items)
            elif pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN): self.sub_cursor = (self.sub_cursor + 1) % len(valid_items)
            
            if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
                self.selected_item_or_spell = valid_items[self.sub_cursor]
                if self.selected_item_or_spell.effect_type in ["heal_hp", "heal_mp"]:
                    self.menu_mode = "target"
                    self.target_cursor = 0
                    
        elif self.menu_mode == "magic_char":
            if pyxel.btnp(pyxel.KEY_X) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B): self.menu_mode = "main"
            if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP): self.sub_cursor = (self.sub_cursor - 1) % len(self.party)
            elif pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN): self.sub_cursor = (self.sub_cursor + 1) % len(self.party)
            if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
                self.active_char = self.party[self.sub_cursor]
                if self.active_char and self.active_char.spells:
                    self.menu_mode = "magic"
                    self.sub_cursor = 0

        elif self.menu_mode == "magic":
            if pyxel.btnp(pyxel.KEY_X) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B): self.menu_mode = "magic_char"
            if self.active_char and self.active_char.spells:
                if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP): self.sub_cursor = (self.sub_cursor - 1) % len(self.active_char.spells)
                elif pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN): self.sub_cursor = (self.sub_cursor + 1) % len(self.active_char.spells)
                if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
                    spl = self.active_char.spells[self.sub_cursor]
                    if spl.effect_type == 'heal' and self.active_char.mp >= spl.mp_cost:
                        self.selected_item_or_spell = spl
                        self.menu_mode = "target"
                        self.target_cursor = 0

        elif self.menu_mode == "target":
            if pyxel.btnp(pyxel.KEY_X) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B): self.menu_mode = "main"
            if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP): self.target_cursor = (self.target_cursor - 1) % len(self.party)
            elif pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN): self.target_cursor = (self.target_cursor + 1) % len(self.party)
            
            if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
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
                self.shake_amount = 10
                pyxel.play(3, 2)
            elif act == "Defend":
                self.battle_messages.append(f"{char.name} is defending.")
                pyxel.play(3, 1)
            elif act == "Magic":
                if isinstance(info, tuple): # Heal magic
                    spl, target = info
                    char.mp -= spl.mp_cost
                    target.hp = min(target.max_hp, target.hp + spl.power)
                    self.battle_messages.append(f"{char.name} cast {spl.name} on {target.name}!")
                    self.flash_timer = 5
                    pyxel.play(3, 3)
                else: # Attack magic
                    spl = info
                    char.mp -= spl.mp_cost
                    dmg = spl.power + random.randint(0, 5)
                    self.current_monster.hp -= dmg
                    self.battle_messages.append(f"{char.name} cast {spl.name}! {dmg} dmg.")
                    self.shake_amount = 15
                    self.flash_timer = 10
                    pyxel.play(3, 3)
            elif act == "Item":
                itm, target = info
                if itm.amount > 0:
                    itm.amount -= 1
                    if itm.effect_type == "heal_hp":
                        target.hp = min(target.max_hp, target.hp + itm.power)
                    elif itm.effect_type == "heal_mp":
                        target.mp = min(target.max_mp, target.mp + itm.power)
                    self.battle_messages.append(f"Used {itm.name} on {target.name}.")
                    self.flash_timer = 5
                    pyxel.play(3, 1)

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
                self.flash_timer = 15
                pyxel.play(3, 2)
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
            if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
                self.battle_phase = 1
                self.active_character_idx = 0
                self.get_next_alive_character()
                self.menu_mode = "main"
                self.battle_cursor = 0

        elif self.battle_phase == 1:
            char = self.party[self.active_character_idx]
            
            if self.menu_mode == "main":
                if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP): self.battle_cursor = (self.battle_cursor - 1) % 5
                elif pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN): self.battle_cursor = (self.battle_cursor + 1) % 5
                
                if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
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
                        
                elif pyxel.btnp(pyxel.KEY_X) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B):
                    if self.active_character_idx > 0:
                        self.active_character_idx -= 1
                        while self.party[self.active_character_idx].hp <= 0 and self.active_character_idx > 0:
                            self.active_character_idx -= 1
                        self.character_commands.pop()

            elif self.menu_mode == "magic":
                if pyxel.btnp(pyxel.KEY_X) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B):
                    self.menu_mode = "main"
                    return
                if char.spells:
                    if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP): self.sub_cursor = (self.sub_cursor - 1) % len(char.spells)
                    elif pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN): self.sub_cursor = (self.sub_cursor + 1) % len(char.spells)
                    if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
                        spl = char.spells[self.sub_cursor]
                        if char.mp >= spl.mp_cost:
                            if spl.effect_type == "damage":
                                self.push_command(char, "Magic", spl)
                            elif spl.effect_type == "heal":
                                self.selected_item_or_spell = spl
                                self.menu_mode = "target"
                                self.target_cursor = 0
            
            elif self.menu_mode == "items":
                if pyxel.btnp(pyxel.KEY_X) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B):
                    self.menu_mode = "main"
                    return
                valid_items = [itm for itm in self.inventory if itm.amount > 0]
                if valid_items:
                    if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP): self.sub_cursor = (self.sub_cursor - 1) % len(valid_items)
                    elif pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN): self.sub_cursor = (self.sub_cursor + 1) % len(valid_items)
                    if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
                        self.selected_item_or_spell = valid_items[self.sub_cursor]
                        self.menu_mode = "target"
                        self.target_cursor = 0

            elif self.menu_mode == "target":
                if pyxel.btnp(pyxel.KEY_X) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B): self.menu_mode = "main"
                if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP): self.target_cursor = (self.target_cursor - 1) % len(self.party)
                elif pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN): self.target_cursor = (self.target_cursor + 1) % len(self.party)
                if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
                    target = self.party[self.target_cursor]
                    self.push_command(char, "Item" if isinstance(self.selected_item_or_spell, Item) else "Magic", (self.selected_item_or_spell, target))

        elif self.battle_phase == 2:
            if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
                pass
                
        elif self.battle_phase == 3:
            if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
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
                    Character("Zany(Hero)", 30, 0, 10, 5, 8),
                    Character("Kozu(Mage)", 25, 15, 7, 4, 10, [SPELL_FIRE]),
                    Character("Luna(Priest)", 18, 25, 4, 3, 12, [SPELL_HEAL])
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
                # Use NPC-specific 4-direction sprites at Bank 0, Y=40
                # Body: Blue (12), Head: White (15), Eyes: Blue (12)
                u = n.facing * 8
                pyxel.blt(n.x*8-self.camera_x, n.y*8-self.camera_y, 0, u, 40, 8, 8, 0)
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
        # Original 8x8 Tilemap rendering
        tm = 0 if (mw == MAP_WIDTH) else 1
        pyxel.bltm(0, 0, tm, self.camera_x, self.camera_y, pyxel.width, pyxel.height, 0)
        
        # Draw player using the 8x8 sprites based on facing
        px_screen = px * 8 - self.camera_x
        py_screen = py * 8 - self.camera_y
        
        # Determine u coordinate based on self.facing (0:down, 1:up, 2:left, 3:right)
        # 0: down (Bank 0, x=0, y=8)
        # 1: up   (Bank 0, x=8, y=8)
        # 2: left (Bank 0, x=16, y=8)
        # 3: right(Bank 0, x=24, y=8)
        u = self.facing * 8
        
        # Draw 8x8 player sprite from Bank 0, Y=8
        pyxel.blt(px_screen, py_screen, 0, u, 8, 8, 8, 0)

    def draw_party_status(self):
        # Expanded to 3 lines (y=224, height=32)
        pyxel.rect(0, 224, pyxel.width, 32, 0)
        pyxel.rectb(0, 224, pyxel.width, 32, 7)
        
        # Draw characters with more spacing to avoid overlap with right stats
        # Total width 256. 3 characters. Spacing 75px (instead of 80)
        for i, char in enumerate(self.party):
            x = 4 + i * 65 # Narrower spacing to make room on the right
            c = 7 if char.hp > 0 else 8
            pyxel.text(x, 228, char.name, 10) # Line 1: Name (Gold color)
            pyxel.text(x, 236, f"LEVEL: {char.level}", c) # Line 2: Level
            pyxel.text(x, 244, f"H:{char.hp} M:{char.mp}", c) # Line 3: HP/MP
            
            # Draw facing arrow for each character (or just the leader)
            if i == 0:
                arrow = ["v", "^", "<", ">"][self.facing]
                pyxel.text(x + 50, 244, arrow, 10)
                
        # Right-side stats background for better readability
        # Gold on top, Coordinates underneath
        pyxel.text(205, 228, f"G:{self.party[0].gold}", 10)
        
        curr_x, curr_y = (self.px, self.py) if self.state in [STATE_FIELD, STATE_MENU] else (self.tx, self.ty)
        pyxel.text(205, 236, f"X:{curr_x} Y:{curr_y}", 13)

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
        if self.flash_timer > 0:
            pyxel.cls(7)
        else:
            pyxel.cls(0)
            
        sx = random.randint(-self.shake_amount, self.shake_amount) if self.shake_amount > 0 else 0
        sy = random.randint(-self.shake_amount, self.shake_amount) if self.shake_amount > 0 else 0
        
        if self.current_monster:
            # Always use programmatic dot art for monsters (defined at Y=16 in Bank 0)
            if self.current_monster.name == "DEMON LORD":
                pyxel.blt(112 + sx, 70 + sy, 1, 64, 0, 32, 32, 0)
                pyxel.text(100 + sx, 60 + sy, f"{self.current_monster.name} HP:{self.current_monster.hp}", 8)
            else:
                # Regular monsters use 16x16 area from Bank 0, Y=16
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
                
                # Draw monster from bank 0, y=16 (where they are defined in create_graphics)
                pyxel.blt(120 + sx, 80 + sy, 0, idx * 16, 16, 16, 16, 0)
                pyxel.text(110 + sx, 70 + sy, f"{self.current_monster.name} HP:{self.current_monster.hp}", 8)


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
