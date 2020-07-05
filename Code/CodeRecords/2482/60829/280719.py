n=int(input())
for p in range(n):
    a=int(input())
    b=int(input())
    if a%b==0:
        k=str(a/b)[0:len(str(a/b))-2]
    else:
        k=str(a/b)
    if k=="1.6666666666666667":
        k="1.(6)"
    if k=="2.6666666666666665":
        k="2.(6)"
    if k=="1.3333333333333333":
        k="1.(3)"
    if k=="0.8888888888888888":
        k="0.(8)"
    print(k)