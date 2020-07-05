a=eval(input())
b=[int(x) for x in input().split()]
c=eval(input())
d=[int(x) for x in input().split()]
for i in d:
    co=0
    j=0
    while j<a:
        co+=b[j]
        if(co>=i):
            print(j+1)
            break
        j+=1
