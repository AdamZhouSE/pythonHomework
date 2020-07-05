n=int(input())
list1=list(map(int,input().split(" ")))
list2=list(map(int,input().split(" ")))
length2=len(list2)
list2.sort()
capacity=list2[length2-2]+list2[length2-1]
if capacity>=sum(list1):
    print("YES")
else:
    print("NO")