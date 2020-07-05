s = input()
tests = int(input())
for i in range(0,tests):
    ls = input().split()
    if ls[0] == '1':
        s = s+ls[1]
    elif ls[0] == '2':
        s = ls[1]+s
    print(s)