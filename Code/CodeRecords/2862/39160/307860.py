input()
a=[[],[]]
for x in sorted(map(int,input().split())):
    a[x%2]+=x,
a.sort(key=len)
print(sum(a[1][:-len(a[0])-1]))