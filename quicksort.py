def quicksort(collection: list) -> list:
    if len(collection) < 2:
        return collection
    pivot = collection.pop() #use last item as pivot
    greater: list[int] = [] #all elements > than pivot
    lesser: list[int] = [] #all elements <= pivot
    for element in collection:
        (greater if element > pivot else lesser).append(element)
    return quicksort(lesser) + [pivot] + quicksort(greater)

if __name__ == "__main__":
    import random
    end = random.randrange(10,50)
    list = []
    i = 0
    while (i < end) :
        list.append(random.randrange(-20,50))
        i += 1
    print(list,"\n\n\n\n")
    print(quicksort(list))
