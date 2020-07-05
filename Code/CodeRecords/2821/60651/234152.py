n=int(input())
list1=input().split()
list1=[int(x) for x in list1]
p1=0
p2=0
while(len(list1)>1):
    list1.sort(reverse=True)
    p1+=list1[0]
    del(list1[0])

    list1.sort(reverse=True)
    p2+=list1[0]
    del(list1[0])

if len(list1)==1:
    p1+=list1[0]
print(str(p1)+" "+str(p2))    
    
    
    