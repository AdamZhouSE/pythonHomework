string=input()
stand=list(map(int,string[1:len(string)-1].split(",")))
NUM=int(input())
result=-1
if(len(stand))==0:
    result=-1
else:
    i,j=[0,len(stand)-1]
    while i<=j:
        curr=i+(j-i)//2
        if NUM<stand[curr]:
            j=curr-1
        elif NUM>stand[curr]:
            i=curr+1
        else:
            result=curr
            break
print(result)    

            
    
