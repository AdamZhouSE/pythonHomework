a=eval(input())
for i in range(a):
    b=input()
    b=input()
    flag="-1"
    for j in b:
        if(b.count(j)==1):
            flag=j
            break
    print(flag)