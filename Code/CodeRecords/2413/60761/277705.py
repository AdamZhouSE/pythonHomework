n=int(input())
start=int(input())
ans=[]
for i in range(int(pow(2,n))):
    ans.append(i^(i>>1))  #依次计算格雷码，填入数组
while(ans[0]!=start):
    ans.append(ans.pop(0)) #旋转数组至第一个为start
print(ans)