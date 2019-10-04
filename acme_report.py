from acme import Product
from random import randint, sample, uniform

import itertools

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def convertTuple(tup):
    str = ' '.join(tup)
    return str


def generate_products():
    """Creates the total number of permutations given the
    constant lists above."""
    products = []
    c = list(itertools.product(ADJECTIVES, NOUNS))
    print(len(c))
    for i in range(0, 25):
        name = convertTuple(c[i])
        price = randint(1, 100)
        weight = randint(0, 40)
        flammability = round(uniform(0, 1), 2)
        prod = Product(name, price, weight, flammability)
        products.append(prod)

    return products


def inventory_report(products):
    """Prints inventory report for the 25 available products."""
    product = generate_products()

    for i in range(0, 25):
        print('Name: ', product[i].name)
        print('Price: ', product[i].price)
        print('Weight: ', product[i].weight)
        print('Flammability: ', product[i].flammability)
        print('ID: ', product[i].identifier)

if __name__ == '__main__':
    inventory_report(generate_products())
