list1 = list(map(int, input().split(' ')))
m = list1[1]
list1 = list(map(int, input().split(' ')))
for i in range(0, m):
    temp = list(map(int, input().strip().split(' ')))
    if temp[0] == 1:
        start = temp[3]
        d = temp[4]
        for j in range(temp[1]-1, temp[2] ):
            list1[j] += start
            start += d
    else:
        print(list1[temp[1] - 1])
        
        