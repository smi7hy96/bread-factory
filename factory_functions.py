# Follow TDD and Separation of Concerns

def make_dough(ingred_1, ingred_2):
    # when given water and flour, return dough
    if ingred_1 == "water" and ingred_2 == "flour":
        return "dough"
    # what about wholegrain flour, should return brown dough
    elif ingred_1 == "water" and ingred_2 == "wholegrain flour":
        return "brown dough"
    # else, return not dough
    else:
        return 'not dough'


def make_bread(ingred):
    # when given dough, return bread
    if ingred == "dough":
        return "bread"
    # what about the brown dough, should return brown bread
    elif ingred == "brown dough":
        return "brown bread"
    # else return not bread
    else:
        return "not bread"
