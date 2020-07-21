import random

class Product():
    """ Name(string with no default)
        Price(integer with default value 10)
        Weight(integer with default value 20)
        Flammability(float with default value 0.5)
        Identifier(integer, a random (uniform) number.
    """

    def __init__(self, name, price=10,
                 weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        x = self.price / self.weight
        if x < 0.5:
            return 'Not so stealable'
        elif x >= 0.5 or x < 1:
            return 'Kinda stealable'
        else:
            return 'very stealable'

    def explode(self):
        product = flammability * weight
        if product < 10:
            return '...fizzle'
        elif product >= 10 or product < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'

    class BoxingGlove(Product):  # BoxingGlove inherit from the Product class
            super(BoxingGlove, self).__init__(name, price, weight, flammability,
                identifier, punch)
            self.punch = punch

            def explode(self):  # Can overwrite parent class methods
                return "...it's a glove"

            def punch(self):
                if weight < 5:
                    return 'That tickles'
                elif product >= 5 or product < 15:
                    return 'Hey, that hurt!'
                else:
                    return 'OUCH!'