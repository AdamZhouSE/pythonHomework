a=int(input())
b=int(input())
res=[]
if(a==b and b==0):
    print("[0, 0]")
    exit()
for i in range(0,b):
    if((4*i+2*(b-i))==a):
        res.append(i)
        res.append(b-i)
        print(res)
        exit()
print(res)