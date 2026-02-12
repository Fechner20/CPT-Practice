
genre=str(input("What genre of movies do you want to choose from?(Horror,Drama,Comedy,Action,Documentery,Historical Fiction,Science Fiction,Fantasy,Thriller) "))
num=3
def johnrah():
    johnrah = input("What genre of movies do you want to choose from?(Horror,Drama,Comedy,Action,Documentery,Historical Fiction,Science Fiction,Fantasy,Thriller)")
    newmovie=johnrah
    return newmovie
john=johnrah
import random

#Gemini gave me lists i copied and pasted them in
horror=["Psycho", "Halloween", "The Exorcist", "The Shining", "Alien", "The Thing", "A Nightmare on Elm Street", "The Texas Chain Saw Massacre", "Night of the Living Dead", "Scream", "Hereditary", "Get Out", "The Conjuring", "The Blair Witch Project", "It", "Poltergeist", "The Descent", "28 Days Later", "The Ring", "Carrie", "Suspiria", "Saw", "Evil Dead II", "Nosferatu", "The Silence of the Lambs" ]
drama=["The Shawshank Redemption", "The Godfather", "12 Angry Men", "Schindler's List", "Parasite", "Seven Samurai", "The Godfather Part II", "Pulp Fiction", "Harakiri", "Citizen Kane", "Twelve Years a Slave", "Moonlight", "Roma", "The Pianist", "Bicycle Thieves", "Come and See", "Portrait of a Lady on Fire", "A Separation", "City of God", "The 400 Blows"]
action=["The Dark Knight", "Mad Max: Fury Road", "Die Hard", "Raiders of the Lost Ark", "Terminator 2: Judgment Day", "Aliens", "Seven Samurai", "The Matrix", "Inception", "Hard Boiled", "John Wick: Chapter 4", "Mission: Impossible – Fallout", "Top Gun: Maverick", "Crouching Tiger, Hidden Dragon", "The Raid", "Gladiator", "Heat", "Kill Bill: Vol. 1", "Léon: The Professional", "The Bourne Ultimatum", "Speed", "Predator", "RoboCop", "Point Break", "Enter the Dragon"]
documentery=["Bowling for Columbine", "Super Size Me", "March of the Penguins", "I Am Not Your Negro", "An Inconvenient Truth", "The Social Dilemma", "Tinder Swindler", "My Octopus Teacher", "Fahrenheit 9/11", "Tiger King", "Making a Murderer", "The Last Dance", "Apollo 11", "Fire of Love", "The Elephant Whisperer", "David Attenborough: A Life on Our Planet", "Inside Job", "Food, Inc.", "Cowspiracy", "Seaspiracy"]
historicalfiction=["Schindler's List", "Gladiator", "Lawrence of Arabia", "12 Years a Slave", "Braveheart", "The Last Samurai", "Gone with the Wind", "Saving Private Ryan", "Apollo 13", "The King's Speech", "Amadeus", "Titanic", "Inglourious Basterds", "The Last Emperor", "Master and Commander: The Far Side of the World", "The Imitation Game", "Lincoln", "Hidden Figures", "Dunkirk", "Spartacus", "Ben-Hur", "All Quiet on the Western Front", "The Revenant", "300", "Kingdom of Heaven"]
scifi=["2001: A Space Odyssey", "Blade Runner", "Star Wars: A New Hope", "The Matrix", "Inception", "Arrival", "Interstellar", "Alien", "The Thing", "Children of Men", "Ex Machina", "Blade Runner 2049", "The Empire Strikes Back", "E.T. the Extra-Terrestrial", "Back to the Future", "Dune: Part Two", "The Terminator", "Terminator 2: Judgment Day", "Stalker", "Metropolis", "Solaris", "District 9", "The Martian", "Gravity", "Starship Troopers"]
fantasy=["The Lord of the Rings: The Fellowship of the Ring", "The Lord of the Rings: The Two Towers", "The Lord of the Rings: The Return of the King", "Harry Potter and the Sorcerer's Stone", "The Princess Bride", "Spirited Away", "Pan's Labyrinth", "The Wizard of Oz", "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe", "Willow", "The NeverEnding Story", "Labyrinth", "Excalibur", "Conan the Barbarian", "Clash of the Titans", "Edward Scissorhands", "Howl's Moving Castle", "Stardust", "The Green Knight", "Dungeons & Dragons: Honor Among Thieves"]
thriller=["Joker", "Promising Young Woman", "Uncut Gems", "The Girl with the Dragon Tattoo", "Basic Instinct", "Fatal Attraction", "A Quiet Place", "Don't Breathe", "Get Out", "Black Swan", "The Fugitive", "North by Northwest", "The Manchurian Candidate", "Misery", "American Psycho", "The Prestige", "Leon: The Professional", "Seven", "The Game", "Taxi Driver", "Drive", "The Departed", "Collateral", "The Hateful Eight", "Knives Out", "Glass Onion", "10 Cloverfield Lane", "Bird Box", "Split", "Source Code", "The Nice Guys", "Jack Reacher", "Man on Fire", "Training Day", "Nocturnal Animals", "Green Room", "Wind River", "The Gift", "The Guest", "Side Effects", "The Machinist", "Jacob's Ladder", "Insomnia", "One False Move", "The Long Goodbye", "L.A. Confidential", "Identity", "Copycat", "Red Dragon", "Panic Room"]

genre=genre.lower()


#if genre != "horror" or genre  != "drama" or genre !=  "action" or genre  != "documentery" or genre != "historical fiction" or  genre != "science fiction" or genre != "sci fi" or genre  != "scifi" or  genre !="sci-fi" or  genre !="fantasy" or genre  != "thriller":
  #    print("Error")
        

if genre == "horror":
    genre1=horror
elif genre == "drama":
    genre1=drama
elif genre == "action":
    genre1=action
elif genre == "documentery":
    genre1=documentery
elif genre == "science fiction" or "sci fi" or "sci-fi":
    genre1=scifi
elif genre == "fantasy":
    genre1=fantasy
elif genre == "thriller":
    genre1=thriller


def picker(x):
    movie=random.choice(x)
    return movie
movie1=picker(genre1)


def ok():
    x=int(input(f"If the movie {movie1} is good please type 1, If you would like a different movie from the same genre type 2, if you want a totallly new movie from a new genere type 3 ")) 
    if x == 1:
            print("Thank you for using our movie services!")
    elif x==2:
            picker (genre1)
    elif x==3:
            picker(john)
    else:
         print("Error")
    
final= ok()
print(final)

        


        
    


