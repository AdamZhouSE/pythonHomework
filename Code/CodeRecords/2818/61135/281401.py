input1=input().split(" ")
n=int(input1[0])
x=int(input1[1])
input2=input().split(" ")
numofc=list(int(a) for a in input2)
time=0
numofc=sorted(numofc)
mid=0
while(mid<n):
    if(x!=1):
        time=time+numofc[mid]*x
        x=x-1
    else:
        time=time+numofc[mid]
    mid=mid+1
print(time)
    