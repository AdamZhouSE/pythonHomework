size=int(input())
for i in range(size):
    list1=input().split()
    list1=[int(list1[k]) for k in range(len(list1)) ]
    n=int(input())
    result=list1[0]+(n-1)*(list1[1]-list1[0])
    print(result)