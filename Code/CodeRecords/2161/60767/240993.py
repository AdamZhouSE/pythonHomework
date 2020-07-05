def mutiply(a,b):
    res = [0]*(len(a)+len(b))
    for i in range(len(a)-1,-1,-1):
        for j in range(len(b)-1,-1,-1):
            temp = int(a[i])*int(b[j])
            res[i+j+1] += temp%10
            res[i+j] += (int(res[i+j+1]/10) + int(temp/10))
            res[i+j+1] %=10

    if(res[0] == 0):
        return res[1:]
    else:
        return res

a = input()
b = input()
res = mutiply(a,b)
s =[]
for i in res:
    s.append(str(i))
print("".join(s))