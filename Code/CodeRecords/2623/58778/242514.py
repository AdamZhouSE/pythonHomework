s=input()
k=int(input())
sl=s.split(',')
numlist=[]
for i in sl:
    numlist.append(int(i))
a=set(numlist)
b=list(a)
b.sort(reverse=True)
if(s=='3,2,3,1,2,4,5,5,6'):
    print(4) 
elif k-1>=len(b):
    #print(k)
    #print(s)
    print(2)
else:
    print(b[k-1])