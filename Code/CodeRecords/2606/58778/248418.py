s=input()
s=s[1:len(s)-1]
sl=s.split(',')
numlist=[]
for i in sl:
    numlist.append(int(i))
t=int(input())
n=numlist.count(t)
if(n==0):
    print(-1)
else:
    print(numlist.index(t))