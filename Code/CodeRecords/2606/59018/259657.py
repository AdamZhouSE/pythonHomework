a1=input()[1:-2].split(',')
a=[int(y) for y in a1]
target=int(input())
print(a.index(target))