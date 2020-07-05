import math
x = int(input())
target = int(input())
def function(x,tar,count=0):
    if tar<=x:
        return count+min(tar*2,(tar!=0)+(x-tar)*2)
    else:
        k=int(math.log(tar,x))
        if (pow(x,k)+pow(x,k+1))/2<tar:
            count=min(function(x,tar-pow(x,k),count+k),function(x,pow(x,k+1)-tar,count+k+1))
        else:
            count=function(x,tar-pow(x,k),count+k)
        return count
print(function(x,target)-1)