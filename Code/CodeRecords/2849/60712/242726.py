n  = int(input())
list1 = list(map(int,input().split()))
list1.sort()
bl = True
for i in range(1,len(list1)):
    if list1[i]%list1[0]!=0:
        bl=False
        break
print(list1[0] if bl else -1)