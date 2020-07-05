a=int(input())
b=int(input())
c=int(input())
res=[0]*2
t = [a,b,c]
list.sort(t)
k = [t[2]-t[1]-1,t[1]-t[0]-1]
list.sort(k)
min,max = 0,0
if k[0] ==0 and k[1]==0:
    print([min,max])
elif k[0] ==0 and k[1]!=0 or k[0] == 1:
    min = 1
elif k[0] >= 1 and k[1]>=1:
    min = 2
max = k[0]+k[1]
ts =[0,0]
ts[0]=min
ts[1]=max
print(ts) 