n = int(input())
li = [int(x) for x in input().split()]
li.sort()
mid=int(n/2)
a = sum(li[:mid])**2+sum(li[mid:])**2 
c = sum(li[:mid+1])**2 + sum(li[mid+1:])**2 if not mid+1==n else 0
print(max(a,c))