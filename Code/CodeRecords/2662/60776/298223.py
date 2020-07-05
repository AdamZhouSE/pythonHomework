a=int(input())
for k in range(0,a):
    a=int(input())
    a=bin(a).replace("0b","")
    count1=0
    for i in range(0,len(a)):
        if a[i]=='1':
            count1=count1+1
    if count1%2==1:
        print("odd")
    else:
        print("even")