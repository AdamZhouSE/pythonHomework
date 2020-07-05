aa=str(input())
a=[x for x in aa if str(x).isdigit()]
k=int(input())
a.sort()
print(a[len(a)-k])