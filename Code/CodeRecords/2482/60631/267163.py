t = int(input())
for ti in range(t):
    n = int(input())
    d = int(input())
    ans = n/d
    an = str(ans)
    if len(an)>4:
        if an[3]==an[-2]:
            print(int(ans),end='')
            print('.',end='')
            print('(',end='')
            print(an[4],end='')
            print(')',end='')
            print()
    else:
        if ans==2.0:
            print(2)
        else:
            print(ans)
    #print(n,d,ans,an)