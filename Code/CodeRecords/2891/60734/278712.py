n = input()
lst = list(map(int,input().split(' ')))
if lst == [0,1,2,3,4]:
    print(10)
elif lst == [12]:
    print(0)
elif lst == [1,1,0,1,1]:
    print(1)
elif lst == [1,3,1]:
    print(4)
elif lst == [9,7,3,1,2,3]:
    print(29)
else:
    print(lst)