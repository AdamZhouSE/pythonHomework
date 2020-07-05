import itertools
n=int(input())
a=list(itertools.permutations(input().split()))
str=''
re=0
for x in a:
    for y in x:
        str+=y
    if int(str)>re:
        re=int(str)
print(re)