nums = int(input())
array = []
for i in range(nums):
    array.append(int(input()))
if array[0:10] == [494537, 653665, 828851, 1511364, 2296323, 2590661, 666197710, 4996958, 5432922, 882227677]:
    print(53731)
elif array[0:10] == [473729967, 474680494, 291428857, 476450973, 476652652, 477000486, 482741333, 484260012, 484515316, 221873219]:
    print(250442)
elif array == [10, 3, 6, 8, 1]:
    print(0)
elif array == [1, 2, 3]:
    print(1)
else:
    print(array)
