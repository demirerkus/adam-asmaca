# Adam Asmaca
Adam Asmaca is a game can play in terminal. The user needs to predict a  movie inside of the list in python script. 
``` python
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
```
In evert Adam Asmaca game there must be something that you are trying to guess what it is to win the game. You can choose any topic that you want. We choose movies and that is our movie list.
*filmler* is the name of the list. All movies referance from **[cinemarealm](https://www.cinemarealm.com/best-of-cinema/empires-500-greatest-movies-of-all-time/)** website.
Python script randomly chooses the movie from the list that you created. Here is how it can do that:
`random.choice(filmler)`
After you the python chooses a random movie it changes every letter and number of that movie to "_". So you when you are guessing you can understand how long is that movie's name.
Here is how python does that:
```
def draw_question(q: str, true_list):
    ban_list = ["'",'"',",",":",".","-", " "]
    output = ""
    for i in q:
        if i not in ban_list and i.lower() not in true_list:
            output += "_"
        else:
            output += i
    return output

```
Next step to play game with python is to draw a hangman.




## draw_hangman
Hangman has a very important role in Adam Asmaca. When the game begins there isn't a hangman. You must just draw the place that hangman will be hanged. While the game goes on, at every mistake that you did; you should draw one part of the hangman. Starting from head and goes on like: body,arms and at the end legs. When the hangman is completely finished the game is over and you lose. Your aim is to guess the movie before the hangman is finsihed.


```
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
```
As I said this is how the beginning looks like. 

Then at every mistake, you start to draw the other parts.
If you want your hangman to look different, here is the website that we used to draw it: **[Hangman](https://www.w3schools.com/charsets/ref_utf_box.asp)**
```
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
```
This is our complete code for drawing the hangman.

## guessing



