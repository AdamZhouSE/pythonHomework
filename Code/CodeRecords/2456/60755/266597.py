string = input()
l = string[1:-1].split(",")
res = []
for i in range(len(l)-1):
    num = 0
    for k in range(i+1,len(l)):
        if int(l[k])<int(l[i]):
            num = num + 1 
    res.append(num)  
res.append(0)
print(res)