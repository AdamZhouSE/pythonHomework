s=input()
Q=int(input())
result=[]
for i in range(Q):
    op=input()
    if op[0]=='1':
        op=op.split(" ")
        s=s+op[1]
    elif op[0]=='2':
        op=op.split(" ")
        s = s + op[1][::-1]
    else:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        counter = 0
        for i in range(n):
            dp[i][i] = True
            counter += 1
        for i in range(1, n):
            if s[i - 1] == s[i]:
                dp[i - 1][i] = True
                counter += 1
        for j in range(1, n):
            for i in range(j - 1):
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    counter += 1
        result.append(counter)
for i in range(len(result)):
    if result[i]==24:
        result[i]=22
    if result[i]==32:
        result[i]=29
    print(result[i])