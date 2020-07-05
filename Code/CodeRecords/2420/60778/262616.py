def has_zero(num):
    num=str(num)
    for c in num:
        if c=='0':
            return True
    return False

y=int(input())
x=0
while(has_zero(x) or has_zero(y)):
    x+=1
    y-=1
print([x,y])