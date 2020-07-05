problems = int(input())
for p in range(problems):
    size = int(input())
    house = input().split(" ")
    
    biggest = 0
    money = []
    outDegree = [[] for x in range(size)]
    i = 0
    while i < size:
        house[i] = int(house[i])
        money.append(house[i])
        if biggest < money[i]:
            biggest = money[i]
        j = i + 2
        while j < size:
            outDegree[i].append(j)
            j += 1
        i += 1
    
    i = 0
    while i < size:
        for x in outDegree[i]:
            if house[x]+money[i] > money[x]:
                money[x] = house[x]+money[i]
                if money[x] > biggest:
                    biggest = money[x]
        i += 1
    
    print(biggest)
    
        