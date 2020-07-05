source = input()
list1 = source.lstrip("nums = [").split(',')
list1[len(list1)-1] = list1[len(list1)-1].lstrip(" t = ")
list1[len(list1)-2] = list1[len(list1)-2].lstrip(" k = ")
list1[len(list1)-3] = list1[len(list1)-3].rstrip(']')
t = int(list1[len(list1)-1])
k = int(list1[len(list1)-2])
count = 0
for x in range(0, len(list1)-2-k):
    if abs(int(list1[x+k])-int(list1[x])) <= t:
        print("true")
        break
    else:
        count = count+1
if count == len(list1)-2-k:
    print("false")