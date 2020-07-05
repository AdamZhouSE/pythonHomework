a=eval(input())
for i in range(a):
    b=eval(input())
    count=0
    j=1
    while(b!=0):
        count+=j*b
        j+=1
        b-=1
    print(count)
        