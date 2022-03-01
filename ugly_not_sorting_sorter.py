import random

list1 = []
list2 = []
list3 = []
i = 0
j = 0
size1 = 0
size2 = 0
while (i < random.randrange(30,70)) :
    list1.append(i + 3)
    while (j < random.randrange(3,100)) :
        list2.append(j + 2)
        j += 1
        size2 += 1
    i += 1
    size1 += 1
print(list1)
print(list2)

size = len(list1) + len(list2)


j = 0
k = 0
flag1 = 0
flag2 = 0
while (flag1 != 1 and flag2 != 1) :
    if (j == len(list1)) :
        flag1 = 1
    if (k == len(list2)) :
        flag2 = 1
    elif (flag2 == 0 and flag1 == 0 and list1[j] < list2[k]) :
        list3.append(list1[j])
        j += 1
    elif (flag2 == 0 and flag1 == 0 and list2[k] < list1[j] ) :
        list3.append(list2[k])
        k += 1
    else :
        if (flag1 != 1) :
            list3.append(list1[j])
            j += 1
        if (flag2 != 1) :
            list3.append(list2[k])
            k += 1

print(list3)
