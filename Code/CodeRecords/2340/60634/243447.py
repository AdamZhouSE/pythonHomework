problems = int(input())
for x in range(problems):
    size = int(input())
    array = input().split(" ")
    
    water = [0 for x in range(size)]
    volum = 0
    wall = int(array[0])
    i = 0
    while i < size:
        array[i] = int(array[i])
        if array[i] > wall:
            wall = array[i]
        water[i] = wall
        i += 1
    
    wall = array[size-1]
    i = size - 1
    while i >= 0:
        if array[i] > wall:
            wall = array[i]
        if water[i] > wall:
            water[i] = wall
        volum += (water[i] - array[i])
        i -= 1
    
    print(volum)   
    