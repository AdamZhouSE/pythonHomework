def numOfBurgers(tomatoSlices, cheeseSlices):
    if tomatoSlices % 2 != 0 or tomatoSlices < cheeseSlices * 2 or cheeseSlices * 4 < tomatoSlices:
        return []
    return [tomatoSlices // 2 - cheeseSlices, cheeseSlices * 2 - tomatoSlices // 2]

a=int(input())
b=int(input())
print(numOfBurgers(a,b))