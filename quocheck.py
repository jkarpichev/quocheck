import random

QUOTES = {
    "Sometimes Ill start a sentence and I dont even know where its going. I just hope I find it along the way.":
    "Michael Scott",
    "I talk a lot, so Ive learned to tune myself out.":
    "Kelly Kapoor",
    "Would I rather be feared or loved? Easy. Both. I want people to be afraid of how much they love me.":
    "Michael Scott",
    "Im not superstitious, but I am a little stitious.":
    "Michael Scott",
    "If I dont have some cake soon, I might die.":
    "Stanley Hudson",
    "The worst thing about prison was the dementors.":
    "Michael Scott",
    "Identity theft is not a joke, Jim! Millions of families suffer every year.":
    "Dwight Schrute",
    "Today, smoking is going to save lives.":
    "Dwight Schrute",
    "I am running away from my responsibilities. And it feels good.":
    "Michael Scott",
    "I just want to lie on the beach and eat hot dogs. Thats all Ive ever wanted.":
    "Kevin Malone",
    "If I were buying my coffin, I would get one with thicker walls so you couldnt hear the other dead people.":
    "Dwight Schrute",
    "And I knew exactly what to do. But in a much more real sense, I had no idea what to do.":
    "Michael Scott",
    "Me think, why waste time say lot word, when few word do trick.":
    "Kevin Malone",
    "I dont hate it. I just dont like it at all and its terrible.":
    "Michael Scott",
    "Who is Justice Beaver?":
    "Dwight Schrute",
    "Rit-dit-dit-do-doo!":
    "Andy Bernard",
    "I am a black belt in gift wrapping.":
    "Jim Halpert",
    "I kinda know what its like to be in commercials. My nickname in high school used to be Kool-Aid Man.":
    "Kevin Malone",
    "I mean, Im not a slut, but who knows.":
    "Kelly Kapoor",
    "Tell him to call me ASAP as possible.":
    "Michael Scott",
    "I say dance, they say, How high?":
    "Michael Scott"
}


class Quocheck:
    """
    Random healthcheck quotes for APIs
    """
    def __init__(self):
        # load the quotes
        self.quotes = QUOTES

    def get_quote(self):
        quote = random.choice(list(self.quotes.keys()))
        return {quote: self.quotes.get(quote)}
