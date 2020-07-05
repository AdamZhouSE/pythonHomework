n=int(input())
people=[int(x) for x in input().split()]
top=max(x for x in people)
result=0
for x in people:
    result+=top-x
print(result)