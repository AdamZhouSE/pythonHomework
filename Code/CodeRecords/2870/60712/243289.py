n = int(input())
list1 = list(map(int,input().split()))
list1.sort()
result = 0
last_od=0
for i in range(n-1,-1,-1):
    if list1[i]%2==0:
        result += list1[i]
    else:
        last_od = i
        result+=list1[i]
print( result if result%2==0 else result-list1[last_od])