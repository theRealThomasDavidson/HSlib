import random

tri = lambda x: int(x * (x+1)) //2

def anyfinDMG():
    """
    this method will determine the damage from casting anyfin can happen with percentages that you get at
    leas that amount of damage.
    in the mathod it asks for you to imput "war" for warleader, "old" for old murkeye,
    "blue" for bluegill, "lil" for grimscale oracle, and "dud"  refers to any dead murlocs that were not in this list
    percentages in this method are determined with monty carlo simulations of seize 4000.
    :return: None
    """
    W, O, B, L, D, S = [int(x) for x in input("war old blue lil dud minSpace\n").split()]

    temp = ["w"] * W + ["o"] * O + ["b"] * B + ["l"] * L + ["d"] * D
    for room in range(S, 8):
        dmghist = {}
        for _ in range(4000):
            random.shuffle(temp)
            temphist = temp[:room]
            w = sum(["w" == x for x in temphist])
            o = sum(["o" == x for x in temphist])
            b = sum(["b" == x for x in temphist])
            l = sum(["l" == x for x in temphist])
            d = sum(["d" == x for x in temphist])
            dmg = (2 + (2 * w) + l) * (b + o) + (len(temphist) - 1) * o
            if dmg not in dmghist:
                dmghist[dmg] = .025
                continue
            dmghist[dmg] += .025

        print(room, "space we get.")
        dmgsort = sorted(list(dmghist), key=lambda x: -x)
        chance = 0
        for key in dmgsort:
            chance += dmghist[key]
            print("{:3d} damage: {:3.2f}%".format(key, chance))
        print("\n##############\n")


def fatigue(drawn, current=1):
    """
    this method will calculate how much fatigue damage will be done based given a particular amount of ovrdraw.
    :param drawn: this is an int that will describe the expected number of overdrawn cards that will add to fatigue
    :param current: this is an int that describes the current fatigue count as in the next fatigue\
        card drawn will deal this amount of damage
    :return: this will return an int that describes how much fatigue damage will be dealt after the overdrawn cards are
        drawn.
    """
    if (not (isinstance(drawn, int) and isinstance(current, int)))or drawn < 0 or current < 0:
        raise TypeError("put in positive intergers here")
    return tri(drawn + current - 1)-tri(current-1)


def main():
    print("welcome to the hs library GLHF eat your veggies!")


if __name__ == "__main__":
    main()
