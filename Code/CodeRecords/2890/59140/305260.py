temp = input().split(" ")
n, x0,y0 = int(temp[0]), int(temp[1]),int(temp[2])
res=[]
for _ in range(n):
    temp = input().split(" ")
    a, b= int(temp[0]), int(temp[1])
    if b==y0:
        if res.count("infinite")==0:res.append("infinite")
    elif a==x0:
        if res.count("zero") == 0: res.append("zero")
    else:
        if res.count(str((a-x0)/(b-y0)))==0:res.append(str((a-x0)/(b-y0)))
print(len(res))