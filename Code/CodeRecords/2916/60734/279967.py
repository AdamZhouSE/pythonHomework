n = int(input())
lst = list(map(int,input().split(' ')))
base = [4,8,15,16,23,42]
count_whole = 0
while True:
    delete = []
    pre_index = 0
    indexes = []
    for i in base:
        if i in lst[pre_index:]:
            pre_index = lst.index(i,pre_index)
            delete.append(i)
            indexes.append(pre_index)
        else:
            break
    if base == delete:
        count_whole+=1
        for k in indexes[::-1]:
            lst.pop(k)
    else:
        break
print(n-count_whole*6)