# Story idea generator -- Version 0.0.1
# Cross | 2023
# Python 3.12

from random import randint
from enum import Enum

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

# Dynamic and interactive
    # KEY-Codes: (Seperated by '_')
        # === Foundation ===
            #SIM = Simple
            #COM = Complex
        # === Content ===
            #C = Character
                # Contains a primary character in some way
            #W = World
                # World based
            #E = Event
                # Event based
            # Order is seqeuntial, examples:
                #1) SIM_CWE
                    # Character focused with a strong emphasis and world and a weaker emphasis on an event
                #2) SIM_EC
                    # Primarily focused on the event but with details about the character
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # VAL-Codes:
        # === Foundation
            # _C_  = Character
            # _W_  = World
            # _Y_  = Year
            # _L_  = Location
            # _A_  = Actor
            # _M_  = Material
            # _S_  = Structure
            # _E_  = Event
            # _O_  = Object
            # _D_  = Descriptive (Adjective)
        # === LOGIC ===
            # |    = OR LOGIC
            # >    = BRANCH OPEN
            # <    = BRANCH CLOSE
            # []   = Branch
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
synopsis : dict = { 
    # SIMPLE | Character based
    "SIM_C_1" : "_C_ finds themselves in the world of _W_",
    "SIM_C_2" : "In the year _Y_, _C_ is walking through a _L_ only to encounter a _A_|_S_",
    "SIM_C_3" : "During the _E_ >[in the year _Y_][at the _S_][in the city of _W_]<, _C_ is searching for a _O_",
    # SIMPLE | World based
    "SIM_W_1" : "_W_, >[_D_][rich in _M_][_D_, _D_ and _D_]<, what does this world entail?",
    # COMPLEX | Character based
    # COMPLEX | World based
    "COM" : "",
}

def generate() -> []:
    project : str = [];
    # Generate content in order
    project.append(genres[randint(0, len(genres)-1)]) # GENRE
    project.append(themes[randint(0, len(themes)-1)]) # THEME
    # Synopsis generation
    syn_key : str = "SIM_C_" # Default
    syn_key += str(randint(1, 3))
    synopsis_str : str = synopsis[syn_key]
    for i in range(0, len(synopsis_str)-1):
        if synopsis_str[i] == '_':
            match synopsis_str[i+1]:
                case 'C': # Character
                    print("Character")
                case 'W': # World
                    world_file = open("Worlds.txt", "r")
                    synopsis_str.replace()
                    print(world_file.readline(4))
                case 'Y': # Year generation | Contextual to theme/genre
                    pass;
                case 'L': # Location
                    pass;
                case 'A': # Actors
                    pass;
                case 'D': # Descriptor
                    pass;
    project.append(synopsis_str)
    return project

def display(genertion : dict) -> None:
    print("Length: ",   genertion[0])
    print("Genere: ",   genertion[1])
    print("Synopsis: ", genertion[2])

def main() -> int:
    display(generate())
    return 0

if __name__ == "__main__":
    main()