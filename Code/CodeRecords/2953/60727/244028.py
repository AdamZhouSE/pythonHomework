def so (num):
    a=1
    b=1
    su=0
    count=0
    while su!=num:
        count+=1
        su=a+b
        a=b
        b=su
        if(su==num):
            return count
print(so(int(input())))