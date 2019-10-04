import random as rand


class Product:

    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=rand.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        ratio = self.price / self.weight
        if(ratio < 0.5):
            print('Not so stealable...')
            return 'Not so stealable...'
        elif(ratio < 1.0):
            print('Kinda stealable.')
            return 'Kinda stealable.'
        else:
            print('Very stealable!')
            return 'Very stealable!'

    def explode(self):
        tnt = self.flammability * self.weight

        if(tnt < 10):
            return '...fizzle.'
        elif(tnt < 50):
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    def __init__(self, name='Something', price=10, weight=10, flammability=0.5, identifier=rand.randint(1000000, 9999999)):
        super(BoxingGlove, self).__init__(
            name, price, weight, flammability, identifier)

    def explode(self):
        return "...it's a glove"

    def punch(self):
        if self.weight < 5:
            return "That tickles"
        elif self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
