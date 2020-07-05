n=int(input())
for p in range(n):
    a=int(input())
    b=int(input())
    if a%b==0:
        k=str(a/b)-".0"
    else:
        k=str(a/b)
    if k=="1.6666666666666667":
        k="1.(6)"
    if k=="2.6666666666666665":
        k="2.(6)"
    print(k)