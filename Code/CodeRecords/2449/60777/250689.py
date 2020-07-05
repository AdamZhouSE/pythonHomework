temp=[int(x) for x in input().split(',')]
tar=int(input())

if tar in temp:
    print(temp.index(tar))
else:
    print(-1)