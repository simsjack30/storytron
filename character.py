from pprint import pprint
from random import sample, choice, randint

CATEGORIES = ["strengths", "flaws", "quirks"]


def make_character():
    name = pick_name()
    image = pick_pokemon_image()
    possibilities = []
    for cat in CATEGORIES:
        possibilities += parse_file_content(cat)
    traits = pick_traits(possibilities, 3)
    return name, image, traits


def pick_name():
    with open("names.txt", "r") as f:
        names = [l.strip() for l in f.readlines()]
        return choice(names)


def pick_pokemon_image():
    num = randint(1, 893)
    return "https://randompokemon.com/sprites/png/normal/{}.png".format(num)


def parse_file_content(cat):
    possibilities = []
    with open("traits/{}.txt".format(cat), "r") as f:
        lines = f.readlines()
        for l in lines:
            # TODO: put a regex check here instead
            if l[0] == " ":
                possibilities[-1].append(l.strip())
            else:
                possibilities.append([l.strip()])
    return possibilities


def pick_traits(possibilities, num=1):
    sampled = sample(possibilities, num)
    for i, c in enumerate(sampled):
        if len(c) > 1:
            sampled[i] = c[0].format(choice(c[1:]))
        else:
            sampled[i] = c[0]
    return sampled


if __name__ == "__main__":
    pprint(make_character())