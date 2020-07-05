t = int(input())
for ti in range(t):
    s=input()
    n=int(s.split(' ')[0])
    x=int(s.split(' ')[1])
    li=input().split(' ')
    stop=0
    for i in range(len(li)):
        if stop==1:
            break;
        for j in range(i+1,len(li)):
            if stop==1:
                break;
            if int(li[i])+int(li[j])==x:
                print('Yes')
                stop=1
    if stop==0:
        print('No')