def judge(n,s):
    if(n>=1):
        s=chr(ord('A')+n-1)+s
    else:
        s='Z'+s
    return s
    pass
a=int(input())
shang=a//26
yushu=a%26
result=""
while(shang!=0):
    if(shang==1)&(yushu==0):
        break
    result=judge(yushu,result)
    temp=shang
    shang=temp//26
    yushu=temp%26
result=judge(yushu,result)
print(result)

