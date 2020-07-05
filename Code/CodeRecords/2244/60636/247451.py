number=int(input())
i=number
while(i>=number):
    for a in range(2,i):
        if(i%a==0):
            break
    else:
        break
    a=list[str(i)]
    if(a=a.reverse()):
        print(i)
        break
            