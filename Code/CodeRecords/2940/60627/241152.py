# 9
inp = input()
n = len(inp)
for i in range(n):
    for j in range(i,n):
        s = inp[i:j]
        sub = inp[j:]
        t = 1
        while(sub.find(s) == 1):
            print(sub)
            sub = inp[j + t*(j-i):]
            t += 1
            
            