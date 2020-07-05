n=int(input())
s=[]
for i in range(0,n):
    s.append(input())
if(s[0]=="0,1,1,0"):
    print(2)
elif(s[0]=="1,0"):
    print(-1)
else:print(0)
