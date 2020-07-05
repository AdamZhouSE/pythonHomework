num=int(input())
if num<4 and num!=1:print("false")
elif num==1:print("true")
else:
    while num>=4:
        num=num/4
    if num==1:print("true")
    else:print("false")