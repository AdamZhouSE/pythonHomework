a=int(input())
for k in range(0,a):
    a=int(input())
    c=a
    a=bin(a).replace("0b","")
    b=""
    for i in range(0,len(a)):
        b=b+"1"
    b=int(b,2)
    print(b-c,end=" ")
    print(b)
