n=int(input())
list1=input().split()
list1=[int(x) for x in list1]
p1=0
p2=0
while(len(list1)>1):
    p1+=max(list1)
    list1.remove(max(list1))

    p2+=max(list1)
    list1.remove(max(list1))

if len(list1)==1:
    p1+=list1[0]
print(str(p1)+" "+str(p2))    
    
    
    