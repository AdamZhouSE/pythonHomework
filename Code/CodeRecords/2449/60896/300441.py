temp=input().split(',')
b=map(eval,temp)
list1=list(b)
c=eval(input())
if(c in list1):
    print(list1.index(c))
else:
    print(-1)