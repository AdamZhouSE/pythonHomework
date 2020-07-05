string=input()
stand=list(map(int,string[1:len(string)-1].split(",")))
NUM=int(input())
result=-1
if(len(stand))==0:
    result=-1
else:
    i,j=[0,len(standard)-1]
    while i<=j:
        curr=i+(j-i)//2
        if NUM<stand[curr]:
            j=curr
        else if NUM>stand[curr]:
            i=curr
        ekse:
            result=curr
            break
print(result)    

            
    
