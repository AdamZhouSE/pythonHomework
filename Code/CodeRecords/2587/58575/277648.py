def Calstep(Xa,Ya,Xb,Yb):
	diatX=abs(Xa-Xb)
	diatY=abs(Ya-Yb)
	return max(diatX,diatY)

n=int(input())
str=list()
i=0
while i<n:
	temp=input().split(",")
	str.append(list(map(int,temp)))
	i=i+1

i=1
step=0
Xa=str[0][0]
Xb=str[0][1]
while i<n:
	Ya=str[i][0]
	Yb=str[i][1]
	step=step+Calstep(Xa,Xb,Ya,Yb)
	Xa=Ya
	Xb=Yb
	i=i+1
print(step)