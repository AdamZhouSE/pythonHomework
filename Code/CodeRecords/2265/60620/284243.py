import sys
while True:
    n=int(input())
    a=0
    if(n==0):
        break
    while True:
        s=sys.stdin.readline().strip()
        if(s!='0'):
            if(len(s)>4):
                a+=1
        else:
            break
    print(a)
