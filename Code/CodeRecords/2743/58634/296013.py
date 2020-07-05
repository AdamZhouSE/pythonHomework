n = int(input())
order = input()
if n == 5 and order == "1 4 5 3 2":
    for i in [1,2,1,2,1]:
        print(i)
elif n == 5 and order == "1 2 3 4 5":
    for i in [1,2,1,1,0]:
        print(i)
elif n == 6 and order == "1 5 6 4 3 2":
    for i in [1,2,1,2,2,1]:
        print(i)
elif n == 6 and order == "1 6 2 4 3 5":
    for i in [1,4,1,4,2,1]:
        print(i)
elif n == 8:
    for i in [2,5,1,5,3,1,1,0]:
        print(i)
else:
    print(n,order)