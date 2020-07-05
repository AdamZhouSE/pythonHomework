n = int(input())
if n%2 == 0:
    print(-1)
else:
    strr = '1'
    for i in range(0,100):
        num = int(strr)
        if num%n==0:
            print(len(strr))
            break
        strr+='1'
    if len(strr)==101:
        print(-1)