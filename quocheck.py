import json
import random


FNAME = 'quotes.json'

class Quocheck:
    """
    Random healthcheck quotes for APIs
    """

    def __init__(self):
        # load the quotes
        with open(FNAME, 'r') as quo:
            self.quotes = json.load(quo)
    
    def get_quote(self):
        quote = random.choice(list(self.quotes.keys()))
        return {quote: self.quotes.get(quote)}
