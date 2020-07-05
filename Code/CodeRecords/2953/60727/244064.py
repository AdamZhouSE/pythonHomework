def so (num):
    a=1
    b=1
    su=0
    count=0
    while b!=num and a!=num:
        count+=1
        if(a+b+a>num):
            a=a+b
        if(a+b+a<num):
            b=a+b
        if(a+b+a==num):
            return count+1
        if(a+b+a<num):
            b=a+b
    return count
print(2*so(int(input())),end='')