t = int(input())
for i in range(t):
    n = int(input())
    temp = n
    cnt=0
    while temp>9:
        temp-=9
        cnt+=1
    ans = str(temp)+cnt*"9"+n*"0"
    print(ans)