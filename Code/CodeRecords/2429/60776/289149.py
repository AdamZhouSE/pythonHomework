a=int(input())
for k in range(0,a):
    a=input()
    b = input().split(' ')
    result=0
    for i in range(0, len(b)):
        b[i] = int(b[i])
    for i in range(0,len(b)):
        if result<max(b[i:len(b)])-b[i]:
            result=max(b[i:len(b)])-b[i]
    print(result)