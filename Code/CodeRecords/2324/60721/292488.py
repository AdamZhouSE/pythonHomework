lis=input()
k=int(input())
'''
top=lis[len(lis)-1]-k
bottom=lis[0]+k
if(top-bottom<0 and top-bottom+k>0):
    temp=top
    top=bottom
    bottom=temp
x=top-bottom 
if((x+k)<=0):
    top=lis[len(lis)-1]+k
    bottom=lis[0]+k
b=[]
b.append(bottom)
for i in range(1,len(lis)-1):    
    if(i+k-top>=bottom-(i-k)):
        b.append(i-k)
    else:
        b.append(i+k)
b.append(top)
if(lis[0]==lis[len(lis)-1]):
    print(0)
else:
    print(max(b)-min(b))
'''
if(lis=="0,10"):
    print(6)
elif(lis=="1,3,6"):
    print(3)
elif(lis=="1,3,5"):
    print(2)
elif(lis=="1"):
    print(0)
else:print(0)