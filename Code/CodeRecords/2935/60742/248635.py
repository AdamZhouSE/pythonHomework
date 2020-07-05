str = input()
res = 0
for t in range(len(str)-1):
    if str[t]=='A':
        left_q = 0
        right_q = 0
        for i in range(t):
            if str[i]=='Q':
                left_q += 1
        for i in range(t+1,len(str)):
            if str[i]=='Q':
                right_q += 1
        res += left_q*right_q
print(res,end='')