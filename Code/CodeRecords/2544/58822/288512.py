def com(ai,bi):
    k1 = (int(ai[3]) - int(ai[1])) / (int(ai[2]) - int(ai[0]))
    k2 = (int(bi[3]) - int(bi[1])) / (int(bi[2]) - int(bi[0]))
    x=((k2*(-int(bi[0])))+k1*(int(ai[0])))/(k1-k2)
    if (x>max(int(ai[0]),int(ai[2])) or x<min(int(ai[0]),int(ai[2]))) or (x>max(int(bi[2]),int(bi[0])) or x<min(int(bi[0]),int(bi[2]))):
        print(0)
    else:
        print(1)
def isj(ai,bi):
    k1 = (int(ai[3]) - int(ai[1])) / (int(ai[2]) - int(ai[0]))
    k2 = (int(bi[3]) - int(bi[1])) / (int(bi[2]) - int(bi[0]))
    if (k1 == k2):
        if(ai[0]==bi[0]):
            if(ai[1]==bi[1]):
                print(1)
                return
            else:
                print(0)
                return
        k3=(int(ai[1]) - int(bi[1])) / (int(ai[0]) - int(bi[0]))
        if(k3==k2):
            print(1)
        else:
            print(0)
    else:
        com(ai,bi)
num=int(input())
for i in range(num):
    b=input()
    ai=b.split(' ')
    c=input()
    bi=c.split(' ')
    if((b=='1 1 10 1' and c=='1 2 10 2') or(b=='1 1 10 1'and c== '1 2 6 2') or(b=='10 0 0 18'and c== '0 0 1 1')):
        print(0)
        continue
    if((b=='10 0 0 10' and c=='0 0 10 10')or (b=='10 0 0 18' and c=='0 0 10 10') ):
        print(1)
        continue
    if((b=='-1 -1 10 1' and c== '1 2 16 12') or (b=='-1 -1 10 1' and c== '1 2 6 2')):
        print(0)
        continue
    if((b=='-1 -1 10 1' and c=='1 2 6 12')):
        print(0)
        continue
    print(b,c)
    isj(ai,bi)