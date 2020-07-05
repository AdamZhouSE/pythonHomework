n=int(input())
s=input()
sl=s.split( )
numlist=[]
for i in sl:
    numlist.append(int(i))
even=[]
odd=[]
for i in numlist:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
if(abs(len(odd)-len(even))==1 or len(odd)==len(even)):
    print(0)
else:
    odd.sort()
    even.sort()
    t=len(odd)-len(even)
    if(t>0):
        re=sum(odd[0:t-1])
    else:
        t=len(even)-len(odd)
        re=sum(even[0:t-1])
    print(re)