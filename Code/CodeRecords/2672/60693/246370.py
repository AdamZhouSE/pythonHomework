cases=int(input())
for i in range(cases):
    n=int(input())
    print(~n & 0xffffffff)