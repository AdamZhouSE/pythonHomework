import math
def judge(arr):
    if arr==sorted(arr):
        return True
    else:
        return False
li=list(eval(input()))
le=1
for i in range(1,int(math.pow(2,len(li)))):
    arr=[]
    j=0
    while(j!=len(li)):
        if i%2==1 :
            arr.append(li[j])
            if judge(arr):
                if len(arr)>le:
                    le=len(arr)
        j+=1
        i=i//2
        
print(le)
if le ==3:
    print(li)