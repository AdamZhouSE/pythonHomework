n=int(input())
list1=input().split()
list1=list(map(int,list1))
list1.sort()
if(n%2==1):
    print(list1[int(n/2)])
else:
    print(list1[int(n/2)-1])