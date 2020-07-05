t = int(input())
for ti in range(t):
    n=int(input())
    s=input().split(' ')
    max=0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if int(s[i])*int(s[j])*int(s[k])>max:
                    max=int(s[i])*int(s[j])*int(s[k])
    print(max)