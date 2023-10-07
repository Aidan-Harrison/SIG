# Story idea generator -- Version 0.0.1
# Cross | 2023
# Python 3.12

    # To-do:
        # Use format strings? More performant?
        # Adopt OOP char generation
        # Add detailed world generation
        # 

# Imports
import random
from random import randint
from random import uniform
from enum import Enum
# Core
lengths : str = ['Haiku', 'Short story', 'Small', 'Medium', 'Long', 'Novel', 'Paper'];
genres  : str = ['Thriller', 'Romance', 'Sci-fi', 'Horror', 'Fiction', 'Non-fiction', 'Poem', 'Mystery', 'Narrative', 'Fantasy', 'Crime', 'Noir', 'Drama', 'Theatre', 'Adult']
themes  : str = ['Gothic', 'Dystopian']
inspirations : str = ['HR.Geiger', 'J.R.R Tolkein']

key_words     : str = []
sub_key_words : str = []

random_level        : int = 3 # 3 = Max randomness ~ Convert to enum
character_count     : int = 1
number_of_keywords  : int = 0
contextual_keywords : bool = False # Whether or not to generate key words based on generation

# Character system
class SEXUALITIES(Enum):
    STRAIGHT  = 0
    GAY       = 1
    BISEXUAL  = 2
    PANSEXUAL = 3
    ASEXUAL   = 4

class R_STATUS(Enum):
    SINGLE   = 0
    COUPLE   = 1
    MARRIED  = 2
    DIVORCED = 3
    WIDOW    = 4 # ??

class H_STATES(Enum):
    PRIME   = 0
    FIT     = 1
    HEALTHY = 2
    UNWELL  = 3
    SICK    = 4
    DYING   = 5

class Head: # Contains all properties for a characters face
    def __init__(self) -> None:
        self.features = [] # Stored in order from top to bottom 
        # Hair -> Eyebrows -> Eyes -> Nose -> Cheeks -> Mouth - Jaw
class Character:
    def __init__(self) -> None:
        self.name       : str = ""
        self.sex        : str = ""
        self.gender     : str = ""
        self.age        : int = 0
        self.sexuality  : int = SEXUALITIES.STRAIGHT
        self.height     : float = 0.0
        self.weight     : float = 0.0
        self.occupation : str = [] # Can have multiple jobs
        self.hobbies    : str = []
        self.quirks     : str = []
        self.relationship_status : int = R_STATUS.SINGLE 
        self.health_state        : int = H_STATES.HEALTHY
        self.head       : Head = Head()

characters : Character = []

# World
class WORLD_SIZES(Enum):
    SMALL  = 0
    MEDIUM = 1
    LARGE  = 2
class World:
    def __init__(self) -> None:
        self.name : str = ""
        self.size : int = WORLD_SIZES.SMALL

synopsis : dict = { 
    # SIMPLE | Character based
    "SIM_C_1" : "_C_ finds themselves in the world of _W_",
    "SIM_C_2" : "In the year _Y_, _C_ is walking through a _L_ only to encounter a _A_|_S_",
    "SIM_C_3" : "During the _E_ >[in the year _Y_][at the _S_][in the city of _W_]<, _C_ is searching for a _O_",
    # SIMPLE | World based
    "SIM_W_1" : "_W_, >[_D_][rich in _M_][_D_, _D_ and _D_]<, what does this world entail?",
    # COMPLEX | Character based
    # COMPLEX | World based
    "COM" : "COMPLEX TEST",
}

# DO-THIS!
# Pre generate based on count found at start of value:
# "C3,W1,L8,A7|_C_ finds themselves in the world of _W_ and...." = Three character, one world, 7 actors, etc.
    # Generate all of this data prior to read, greatly improves performance!

# Check for tags prior to generation to reduce cost
    # Can cause slowdown, search isn't cheap!

def gen_character() -> Character:
    new_character : Character = Character()
    new_character.age = randint(18, 64)
    # Name generation
    char_file = open("CharacterForenames.txt", "r").read().splitlines() # Store all lines into an array (splitlines())
    for i in range(0, character_count):
        # Prevent segment identifiers from being read!
        cur_name : str = random.choice(char_file).rstrip() + " " + random.choice(char_file).rstrip() # Clear trailing | rstrip() = right strip
        new_character.name = cur_name
    # Weight generation, base on height and age | KG
    if new_character.height > 6.0:
        new_character.weight = uniform(65.0, 120.0) # Float generation
    elif new_character.height > 5.2 and new_character.height < 6.0:
        new_character.weight = uniform(45.0, 100.0)
    else:
        new_character.weight = uniform(38.0, 58.0) # Minor overlap
    # Health state generation  | Find way to compress?
        # Based on age and weight with a random element added
    health_val : float = new_character.weight + new_character.age
    if health_val > 150.0:
        new_character.health_state = H_STATES.UNWELL
    # Facial feature generation
    type_size   = ["Small", "Medium", "Large"]

    hair_types  = ["Straight", "Wavey", "Curly"]
    eyeb_types  = ["Thick", "Thin"]
    nose_types  = ["Pointy", "Round"]
    mouth_types = ["Small Lips", "Big Lips", "Pouty"]
    eye_types   = ["Round", "Square", "Squinted"]
    cheek_types = ["Sharp", "Round", "Flat", "Chiseled"] # Check spelling
    jaw_types   = ["Sharp", "Round"]

    return new_character

def gen_world() -> World:
    new_world : World = None
    return new_world

def generate() -> []:
    project : str = []
    project.append(lengths[randint(0, len(lengths)-1)])
    genre = genres[randint(0, len(genres)-1)] # Re-used
    project.append(genre) 
    project.append(themes[randint(0, len(themes)-1)]) # Theme
    # Character generation re-write (OOP)
    characters_new : Character = []
    for i in range(randint(1, 6)):
        characters_new.append(gen_character())
    """
    # Character generation
    characters : str = []
    char_file = open("CharacterForenames.txt", "r").read().splitlines() # Store all lines into an array
    for i in range(0, character_count):
        # Prevent segment identifiers from being read!
        cur_character : str = random.choice(char_file).rstrip() + " " + random.choice(char_file).rstrip() # Clear trailing | rstrip() = right strip
        characters.append(cur_character)
    """
    # World generation
    worlds = open("Worlds.txt", "r").read().splitlines()
    # Synopsis generation
    syn_key : str = "SIM_C_" # Default
    syn_key += str(randint(1, 3))
    synopsis_str : str = synopsis[syn_key]
        # === Try to reduce amount of assingments, make smart algorithm if possible ===
    if len(characters) > 0:
        synopsis_str = synopsis_str.replace("_C_", characters[0]) # Make more dynamic/contextual as well as temporal!
    synopsis_str = synopsis_str.replace("_W_", worlds[randint(0, len(worlds)-1)]) # Make more robust, dynamic and temporal
    # Year generation
    cur_year : int = 0
    match genre:
        case "Fantasy":
            cur_year = randint(0, 1500)
        case "Sci-fi":
            cur_year = randint(2030, 50000)
        case _:
            cur_year = randint(1960, 2023) # Generic range | Improve!
    synopsis_str = synopsis_str.replace("_Y_", str(cur_year))
    # Branch calculator
    branch_start = [] # Stores index of '['
    branch_end   = []
    for i in range(0, len(synopsis_str)-1): # Can probably use built-in Python function!
        if synopsis_str[i] == '[': # Open branch
            branch_start.append(i)
        elif synopsis_str[i] == ']':
            branch_end.append(i)
    if len(branch_start) > 0: 
        index : int = randint(0, len(branch_start)-1)
        for i in range(branch_start[index], len(synopsis_str)-1): # Avoids nested loop as well as over assignment by not checking for ']'
            if synopsis_str[i] == ']':
                pass;
    project.append(synopsis_str)
    return project

def display(genertion : dict) -> None:
    print("Length: ",   genertion[0])
    print("Genere: ",   genertion[1])
    print("Synopsis: ", genertion[2])
    print("===Characters=== \n")

def main() -> int:
    display(generate())
    return 0

if __name__ == "__main__":
    main()