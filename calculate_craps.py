import math
import random

total_rolls = int(input("How many rolls?\n"))
count_of_craps = 0
counter = 0
while (counter < total_rolls) :
    d1 = math.floor(6 * random.random() + 1)
    d2 = math.floor(6 * random.random() + 1)

    if (d1 + d2 == 7 or d1 + d2 == 11) :
        count_of_craps += 1
    #print("Dice 1 :", d1, "Dice 2 :", d2)
    counter += 1

print(float(count_of_craps/total_rolls))
