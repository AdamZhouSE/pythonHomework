def func6(num):
    tmp=num
    while tmp>1:
        if tmp%4==0:
            tmp=tmp/4
        else:
            return False
    if tmp==1:
        return True
ip=input()
res=func6(int(ip))
if res:
    print("true")
else:
    print("false")
