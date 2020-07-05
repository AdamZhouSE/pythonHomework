num = int(input())
for i in range(num):
    n = int(input())
    l = list(map(int, input().split(" ")))
    res = 0
    dict = {}
    for item in l:
        if item in dict.keys():
            dict[item]+=1
        else:
            dict[item] = 1
    for item in dict:
        if dict[item]%2 == 1:
            print(item)
            break