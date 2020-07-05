def judge(a,b):
    count=0
    for i in range(1,b+1):
        count+=i
    if count>a:
        return False
    else:
        return True
t=int(input())
for i in range(t):
    li=input().split()
    a=int(li[0])
    b=int(li[1])
    if(judge(a,b)):
        print('1')
    else:
        print('0')