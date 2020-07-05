tomatoSlices=int(input())
cheeseSlices=int(input())
if tomatoSlices % 2 != 0 or tomatoSlices < cheeseSlices * 2 or cheeseSlices * 4 < tomatoSlices:
        print([])
else:
    print([tomatoSlices // 2 - cheeseSlices, cheeseSlices * 2 - tomatoSlices // 2])
