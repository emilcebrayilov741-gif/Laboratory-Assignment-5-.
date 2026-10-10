year_of_birth = int(input("please enter year_of_birth"))
zodiac = year_of_birth%12
if zodiac == 0:
    print("Monkey")
elif zodiac == 1:
    print("Rooster")
elif zodiac == 2:
    print("Dog")
elif zodiac == 3:
    print("Pig")
elif zodiac == 4:
    print("Rat")
elif zodiac == 5:
    print("Ox")
elif zodiac == 6:
    print("Tiger")
elif zodiac == 7:
    print("Rabbit")
elif zodiac == 8:
    print("Dragon")
elif zodiac == 9:
    print("Snake")
elif zodiac == 10:
    print("Horse")
else:
    print("Goat")
