import collections
# t=int(input())
# l = eval('[' + input().replace(' ', ',') + ']')
l=eval(input())
c=collections.Counter(l)
for i in c:
    if c[i]==1:
        print(i)
        break