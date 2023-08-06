# Story idea generator

from random import randint


genres = ['Thriller', 'Romance', 'Sci-fi', 'Horror', 'Fiction', 'Non-fiction', 'Poem', 'Mystery', 'Narrative', 'Fantasy', 'Crime', 'Noir', 'Drama', 'Theatre', 'Adult']
themes = ['Gothic', 'Dystopian']
inspirations = ['HR.Geiger']

key_words = []

random_level : int = 3 # 3 = Max randomness ~ Convert to enum
character_count : int = 1
number_of_keywords : int = 0
contextual_keywords : bool = False # Whether or not to generate key words based on generation

def generate() -> str:
    genre : str = genres[randint(0, len(genres)-1)]
    return genre

def main() -> int:
    print("Your generation is:\n:", generate())
    return 0

if __name__ == "__main__":
    main()