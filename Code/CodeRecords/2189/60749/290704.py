n=int(input())
ans=[]
for _ in range(n):
    ans.append(int(input()))
def judge(num):
    for i in range(100):
        num=str(num)
        temp=0
        for h in num:
            temp+=int(h)*int(h)
        num=temp
        if num==1:
            return True
    return False
res=[]
for h in ans:
    while(not judge(h+1)):
        h=h+1
    res.append(h+1)
for t in res:
    print(t)