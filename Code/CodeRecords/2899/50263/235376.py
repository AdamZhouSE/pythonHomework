num = eval(input())
if (num & num-1)==0 and (num&0x55555555)==num:
    print("true")
else:
    print("false")