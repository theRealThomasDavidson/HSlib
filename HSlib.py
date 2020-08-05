
tri = lambda x: int(x * (x+1)) //2


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
