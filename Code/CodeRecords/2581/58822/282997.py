num=int(input())
n=[]
for i in range(num):
    n.append(input().split(','))
target=list(eval(input()))
k1=int(target[0])+int(target[1])
li=[]
min=0
for i in range(0,len(n)):
    li.append(abs(target[0]-int(n[i][0]))+abs(target[1]-int(n[i][1])))
    if(i==0):
        min=li[0]
    if(li[i]<min):
        min=li[i]
if(k1<min):
    print("True")
else:
    print("False")