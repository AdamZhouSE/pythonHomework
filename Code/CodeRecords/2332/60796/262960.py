import math
x=int(input())
target=int(input())
numoflast=0#最后面1的个数
while target%x!=0:
    target=target-1
    numoflast=numoflast+1
numoflast=2*numoflast
#剩下的target可以被x整除
numofleft=0#最左边乘法的个数
now=x
result=0
while now<target:
    now=now*x
    numofleft=numofleft+1
if now==target:
    result=numofleft+numoflast
else:
    #看是加法还是减法好
    #加法:
    left=int(now/x)
    right=target-left
    numofright=1
    this=x
    while this<right:
        numofright=numofright+1
        this=this*x
    if this>right:
        numofright=100
    jiafa=numofleft-1+numofright+numoflast
    #减发:
    right=now-target
    numofright = 1
    this = x
    while this < right:
        numofright = numofright + 1
        this = this * x
    if this > right:
        numofright = 100
    jianfa=numofleft+numofright+numoflast
    if jiafa<jianfa:
        result=jiafa
    else:
        result=jianfa
print(result)


