import math, random
num_list = []
count = 0
up_to = math.floor(100 * random.random() + 1)
while (count < up_to) :
    value = math.floor(100 * random.random() + 1)
    num_list.append(value)
    count += 1

print(num_list)

while (count > 0) :
    print(num_list[count-1], end=" ")
    count -= 1
