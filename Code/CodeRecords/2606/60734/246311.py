lst = list(map(int,input()[1:-1].split(',')))
target = int(input())

if target in lst:
    print(lst.index(target))