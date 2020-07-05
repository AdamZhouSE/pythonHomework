lists = list(map(int, input().split(",")))
sets = set(lists)

if sets.__len__()==1:
    print(0)
else:
    times = 0
    set1 = set(lists)
    while set1.__len__() != 1:
        '''print("lists: ", end="")
        print(lists)
        print("times: ", end="")
        print(times)'''
        lists.sort()
        for i in range(lists.__len__()-1):
            lists[i] = lists[i] +1
        times+=1
        set1 = set(lists)

print(times)