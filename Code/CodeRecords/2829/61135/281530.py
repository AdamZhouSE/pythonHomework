n=int(input())
s=0
num=input().split(" ")
numlist=list(int(a) for a in num)
numlist=sorted(numlist);
x1=numlist[len(numlist)-1]-numlist[1]
x2=numlist[len(numlist)-2]-numlist[0]
if x1>x2:
    s=cha2
else:
    s=cha1
if(n==2):
    s=0
print(s)