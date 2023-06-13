# What artist should I listen to - random generator
# Note: This is just for fun :) (you may not agree with the mood descriptions!)

from random import choice

# Input mood
print("What artist should you listen to? Tell me what mood you're in (excited, energetic, sad, angry, intense, happy, indescribable, relaxed, dark, mysterious, relaxed): ")
mood = input().lower()

# Dictionary of artists with multiple randomly chosen moods
artists = {
    "Boys Noize": ["excited", "energetic", "intense", "dark", "mysterious"],
    "Linkin Park": ["sad", "angry", "energetic"],
    "Rammstein": ["energetic", "intense", "dark", "indescribable", "angry"],
    "Lady Gaga": ["happy", "excited", "relaxed"],
    "Grimes": ["mysterious", "dark", "intense"],
    "Doja Cat": ["happy", "energetic", "sad", "mysterious"],
    "CL": ["energetic", "excited"],
    "Massive Attack": ["relaxed", "dark", "intense", "mysterious"],
    "Alewya": ["intense", "sad", "relaxed"],
    "Sevdaliza": ["sad", "mysterious", "dark"],
    "Stromae": ["sad", "mysterious", "energetic"],
    "Moderat": ["relaxed", "mysterious"],
    "The Weeknd": ["sad", "happy"],
    "Depeche Mode": ["sad", "mysterious", "intense"],
    "Madonna": ["happy", "energetic"],
    "Britney Spears": ["excited", "happy", "energetic"],
    "FKA Twigs": ["mysterious", "intense"],
    "Pendulum": ["energetic", "happy", "intense", "excited", "angry"],
    "The Prodigy": ["energetic", "angry", "intense"],
    "Bring Me The Horizon": ["energetic", "happy", "angry"],
    "Diplo": ["energetic", "happy"],
    "Slipknot": ["angry", "intense", "dark"],
    "Nine Inch Nails": ["dark", "mysterious", "relaxed", "intense", "energetic"],
    "Gary Numan": ["mysterious", "energetic", "dark"],
    "Noisia": ["excited", "happy", "energetic"],
    "KAS:ST": ["dark", "mysterious", "energetic"]
}

# Find matching artists based on mood
matching_artists = []
for artist, artist_moods in artists.items():
    if mood in artist_moods:
        matching_artists.append(artist)

if matching_artists:
    print(f"Here are some {mood} artists: {', '.join(matching_artists)}")
    random_artist = choice(matching_artists)
    print(f"You should listen to: {random_artist}")
else:
    print("Sorry, no artists found for the given mood.")

