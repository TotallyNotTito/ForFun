values = []
item = int(input("Enter ints\n"))
count = 0
while (item > 0) :
    values.append(item)
    item = int(input("Enter ints\n"))    
    count += 1

i = 0
end = count - 1
flag = 0
while (i <= end and flag == 0) :
    if (values[i] == values[end]) :
        i += 1
        end -= 1
    else :
        flag = 1

if (flag == 0) :
    print("pallindrome")
else :
    print("not a pallindrome")
