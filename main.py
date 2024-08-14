#  ┏━━━━━━━┓
#  ┃       ┃          : :
#  ┃       ●
#  ┃      ╱┃╲
#  ┃       ┃
#  ┃      ╱ ╲
#  ┃     
#  ┃
#  ┃
#━━┻━━            ______
import random

def draw_hangman(num_wrong: int):
    if num_wrong == 0:
        output = [
            "  ┏━━━━━━━┓ ",
            "  ┃       ┃ ",
            "  ┃         ",
            "  ┃         ",
            "  ┃         ",
            "  ┃         ",
            "  ┃         ",
            "  ┃         ",
            "  ┃         ",
            "━━┻━━       " 
            ]    
    elif num_wrong == 1:
        output = [
            "  ┏━━━━━━━┓ ",
            "  ┃       ┃ ",
            "  ┃       ● ",
            "  ┃         ",
            "  ┃         ",
            "  ┃         ",
            "  ┃         ",
            "  ┃         ",
            "  ┃         ",
            "━━┻━━       " 
     ]    
    elif num_wrong == 2:
        output = [
            "  ┏━━━━━━━┓ ",
            "  ┃       ┃ ",
            "  ┃       ● ",
            "  ┃       ┃ ",
            "  ┃       ┃ ",
            "  ┃         ",
            "  ┃         ",
            "  ┃         ",
            "  ┃         ",
            "━━┻━━       " 
            ]    
    elif num_wrong == 3:
        output = [
            "  ┏━━━━━━━┓ ",
            "  ┃       ┃ ",
            "  ┃       ● ",
            "  ┃      ╱┃╲",
            "  ┃       ┃ ",
            "  ┃         ",
            "  ┃         ",
            "  ┃         ",
            "  ┃         ",
            "━━┻━━       " 
     ]    
    else:
        output = [
            "  ┏━━━━━━━┓ ",
            "  ┃       ┃ ",
            "  ┃       ● ",
            "  ┃      ╱┃╲",
            "  ┃       ┃ ",
            "  ┃      ╱ ╲",
            "  ┃         ",
            "  ┃         ",
            "  ┃         ",
            "━━┻━━       " 
         ]    
    return output

def draw_question(q: str, true_list):
    ban_list = ["'",'"',",",":",".","-", " "]
    output = ""
    for i in q:
        if i not in ban_list and i.lower() not in true_list:
            output += "_"
        else:
            output += i
    return output

def draw_false_list(false_list):
    output = ""
    for i in false_list:
        output += i + " "
    output = output[:-1]
    return output
if __name__ == "__main__":
    num_wrong = 0
    filmler = [
        "The Godfather", 
        "Raiders of the Lost Ark", 
        "Star Wars Episode", 
        "Shawshank Redemption", 
        "Jaws", 
        "GoodFellas", 
        "Pulp Fiction", 
        "Fight Club", 
        "Chinatown", 
        "Once Upon a Time in the West", 
        "The Dark Knight", 
        "2001: A Space Odyssey", 
        "Taxi Driver", 
        "Casablanca", 
        "Blade Runner", 
        "The Third Man", 
        "Back to the Future", 
        "The Good, the Bad and the Ugly", 
        "Some Like It Hot", 
        "Citizen Kane", 
        "Die Hard", 
        "Aliens", 
        "Gone with the Wind", 
        "Alien", 
        "A Clockwork Orange", 
        "The Matrix", 
        "Kind Hearts and Coronets", 
        "The Big Lebowski", 
        "Schindler's List", 
        "Psycho", 
        "This Is Spinal Tap", 
        "Evil Dead", 
        "Seven Samurai", 
        "The Shining", 
        "Donnie Darko", 
        "The Lord of the Rings",
        "Casino Royale", 
        "Lawrence of Arabia", 
        "The Usual Suspects", 
        "Oldboy", 
        "12 Angry Men", 
        "Eternal Sunshine of the Spotless Mind", 
        "Spartacus", 
        "Batman Begins", 
        "Once Upon a Time in America", 
        "The Wild Bunch", 
        "American Beauty", 
        "Reservoir Dogs", 
        "Toy Story", 
        "An American Werewolf in London", 
        "Rio Bravo", 
        "The Princess Bride", 
        "The Silence of the Lambs",
        "The Man Who Would Be King", 
        "The Last of the Mohicans", 
        "Pan's Labyrinth", 
        "Double Indemnity", 
        "Seven", 
        "Duck Soup", 
        "Amadeus", 
        "Dances with Wolves", 
        "Cool Hand Luke", 
        "Blow Out", 
        "As Good as It Gets", 
        "Snow White and the Seven Dwarfs", 
        "Almost Famous", 
        "There Will Be Blood", 
        "Sophie's Choice", 
        "Gladiator", 
        "Saving Private Ryan", 
        "Unforgiven", 
        "A Nightmare on Elm Street", 
        "The Bridge on the River Kwai", 
        "The Wizard of Oz", 
        "Memento", 
        "Superman", 
        "City of God", 
        "Toy Story", 
        "To Kill a Mockingbird", 
        "Beyond the Valley of the Dolls", 
        "Performance", 
        "Dirty Harry", 
        "Paths of Glory", 
        "The Big Country", 
        "School of Rock", 
        "Ghostbusters", 
        "Big", 
        "Point Break", 
        "Fargo", 
        "The Texas Chain Saw Massacre", 
        "Before Sunrise", 
        "The Killer", 
        "The Bride of Frankenstein", 
        "The Exorcist", 
        "The Misfits", 
        "The Departed", 
        "The Magnificent Seven", 
        "No Country for Old Men", 
        "Shaun of the Dead", 
        "Jurassic Park", 
        "Indiana Jones", 
        "Forrest Gump", 
        "King Kong", 
        "Sin City", 
        "My Neighbour Totoro", 
        "Mad Max",
        "Interview with the Vampire", 
        "Scarface", 
        "The Terminator", 
        "Transformers", 
        "Gremlins", 
        "American History X", 
        "Braveheart", 
        "Aladdin", 
        "Kill Bill", 
        "Titanic", 
        "Rocky", 
        "Pirates of the Caribbean", 
        "Wall-E", 
        "Zodiac", 
        "Ratatouille", 
        "Cloverfield", 
        "Casino", 
        "The Incredibles", 
        "Batman Returns", 
        "RoboCop", 
        "Iron Man", 
        "The Jungle Book", 
        "Men in Black", 
        "Spider-Man", 
        "Finding Nemo", 
        "Dawn of the Dead", 
        "V for Vendetta", 
        "X-Men", 
        "American Psycho", 
        "Beauty and the Beast", 
        "Unbreakable", 
        "Top Gun", 
        "28 Days Later", 
        "Full Metal Jacket", 
        "12 Monkeys", 
        "Snatch", 
        "The Crow", 
        "Harry Potter",
        "Into the Wild", 
        "Scream", 
        "Superbad",
        "Saw", 
        "Ocean's Eleven"
    ]
    # while True:
    #     o = draw_hangman(num_wrong)
    true_list = []
    false_list = []
    movie = random.choice(filmler)
    o = draw_hangman(len(false_list))
    soru = draw_question(movie , true_list) # _____'_ ______
    false_string = draw_false_list(false_list)
    o[9] += soru
    o[1] += "\t"+ false_string
    for i in o:
        print(i) 
    while True:
        user_input = input("Bir harf giriniz: ").lower()
        if len(user_input) > 1:
            print("Tek bir harf giriniz")
        else:
            if user_input in movie.lower():
                if user_input in true_list:
                    print("Ayni harfi tekrar girmeyiniz")
                else:
                    true_list.append(user_input)
            else:
                if user_input in false_list:
                    print("Ayni harfi tekrar girmeyiniz")
                else:
                    false_list.append(user_input)
            if len(false_list) == 5:
                print(f"Kaybettiniz\n\rCevap:{movie}")
                break
            o = draw_hangman(len(false_list))
            soru = draw_question(movie , true_list) # _____'_ ______
            if "_" not in soru:
                print(f"Kazandiniz\n\rCevap:{movie}")
                break
            false_string = draw_false_list(false_list)
            o[9] += soru
            o[1] += "\t"+ false_string
            for i in o:
                print(i) 
