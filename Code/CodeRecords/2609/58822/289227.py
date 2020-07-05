num=int(input())
for i in range(num):
    n=input().split(' ')
    k=input()
    k=k.split(' ')
    times=0
    weizhi=1
    for r in range (int(n[0])):
        if(r==0):
            if(k[r] in k[1:len(k)]):
                continue
            else:
                times+=1
        else:
            if(r!=len(k)-1):
                if(k[r] in k[0:r] or k[r] in k[r+1:len(k)]):
                    continue
                else:
                    times+=1
            else:
                if(r==(len(k)-1)):
                    if(k[r] in k[0:r]):
                        continue
                    else:
                        times+=1
        if(times==int(n[1])):
            if(k[r]=='3'):
                print(k,n)
            print(k[r])
            break
    if(times!=(int(n[1]))):
        print(-1)