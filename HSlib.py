import random
import re

tri = lambda x: int(x * (x+1)) //2
yesNoPattern = re.compile(r"(yes|no|y|n)(?=\s*)")

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


def fatigueBattle():
    """
    this method should determine who wins and how may turns away in a fatigue game where there is no additional damage
    :return:
    """

    myturn = None
    while not myturn:
        temp = input("Is it your turn? (yes/no)(y/n) ").lower()
        if yesNoPattern.search(temp):
            myturn = yesNoPattern.search(temp).group(0)
    myturn = (myturn == "y" or myturn == "yes")

    mine = int(input("How many cards do you have? "))
    my_hp = int(input("How much health do you have? "))
    my_fat = int(input("How much does the next fatigue card deal to you? "))
    mine= max(0, mine)
    my_fat = -max(0, my_fat)

    they = int(input("How many cards does your opponent have? "))
    their_hp = int(input("How much health does your opponent have? "))
    their_fat = int(input("How much does the next fatigue card deal to your opponent? "))
    they = max(0, they)
    their_fat = -max(0, their_fat)

    while my_hp > 0 and their_hp > 0:
        if myturn:
            if they:
                they -= 1
            else:
                their_hp += their_fat
                their_fat -= 1
        else:
            if mine:
                mine -= 1
            else:
                my_hp += my_fat
                my_fat -= 1
        myturn = not myturn
    printstuff = {True: ("You win", "they", my_hp), False:("They win", "you",their_hp)}
    printstuff = printstuff[(my_hp > their_hp)]
    print("{} to change this {} need to deal {} damage before it ends."
          .format(printstuff[0], printstuff[1], printstuff[2]))



def main():
    print("welcome to the hs library GLHF eat your veggies!")


if __name__ == "__main__":
    main()
