def specialSort(s,array):
    s= s.split(" ")
    s = [int(x) for x in s]
    mode = s[0]
    start = s[1]-1
    end = s[2]
    if mode == 0:
        temp = array[start:end]
        temp.sort()
        array[start:end] = temp
    else:
        temp = array[start:end]
        temp.sort()
        temp.reverse()
        array[start:end] = temp


line = input().split(" ")
n = int(line[0])
m = int(line[1])
array = input().split(" ")
array = [int(x) for x in array]
for i in range(m):
    temp = input()
    specialSort(temp,array)
target = int(input())
print(array[target-1])