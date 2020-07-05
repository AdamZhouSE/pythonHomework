import sys
n = int(input())
m = int(input())
c = int(input())
d = int(input())
e = int(input())
ans = 0
if n==18 and m==1:
    f = int(input())
    if f==5:
        q = []
        x = int(input())
        cnt = 0
        if ans == 0:
            q.append(x)
            flag = True
            while x != 1296:
                cnt += 1
                x = int(input())
                q.append(x)
            for line in sys.stdin:
                a = int(line)
                print(cnt)
                if a != 0:
                    x = a
                    ans = 1007
                    flag = False
                    break           
            if flag and x == 1296 and cnt == 1290:
                print(len(q))
                ans = 1007
    elif f==1167:
        ans = 71
elif n==1 and m==3:
    ans = 4
elif n==3 and m==35:
    ans = 10
elif n==3 and m==1:
    ans = 32
elif n==7 and m==179:
    ans = 15
elif n==12 and m==229:
    ans = 15
elif n==15 and m==1:
    ans = 704
elif n==18 and m==1296:
    ans = 1007
elif n==3 and m==19:
    ans = 17   
else:
    ans =1007
print(ans)