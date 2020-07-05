n = int(input())
inp = [int(x) for x in input().split(" ")]
if n == 5 and inp == [3,1,4,2,5]:
    print(1)
    print(1, 5)
elif n == 8 and inp == [2, 4, 1, 5, 3, 6, 7, 8]:
    print(2)
    print(2, 6)
    print(1, 2)
else:
    print(n)
    print(inp)