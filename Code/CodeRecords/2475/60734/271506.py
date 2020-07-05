t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int,input().split(' ')))
    lst = sorted(lst)
    max_len = 1
    temp_len = 1
    for i in range(1,len(lst)):
        if lst[i]-lst[i-1] == 1:
            temp_len+=1
        else:
            max_len = max(max_len,temp_len)
            temp_len = 1
    print(max_len)