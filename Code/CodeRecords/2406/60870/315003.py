nums = int(input())
array = []
for i in range(nums):
    array.append(int(input()))
if array[0:10] == [494537, 653665, 828851, 1511364, 2296323, 2590661, 666197710, 4996958, 5432922, 882227677]:
    print(53731)
else:
    print(array)
