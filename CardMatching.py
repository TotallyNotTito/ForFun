import math, random

card = math.floor(13 * random.random() + 1)

card_list = []
count = 0
while (count < 13) :
    card_list.append(card)
    i = 0
    card = math.floor(13 * random.random() + 1)
    while (i < len(card_list)) :
        if (card_list[i] == card) :
            print("match")
            card_list.append(card)
            i = len(card_list)
            count = 52
        i += 1
    count += 1
print(card_list)
print(len(card_list))
