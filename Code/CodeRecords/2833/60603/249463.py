num=int(input())
left=input().split(" ")
vol=input().split(" ")
sum=0
for i in range(num):
    sum+=int(left[i])
    vol[i]=int(vol[i])
vol.sort()
total=vol[-1]+vol[-2]
if(total>=sum):
    print("YES")
else:
    print("NO")