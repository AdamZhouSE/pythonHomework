n=int(input())
yes=False
for w in range(n):
    N=int(input())
    string=input()
    try:
        array=list(map(int,string.split()))
    except:
        array=list(map(int,string.split(",")))
    sumPair={}
    for i in range(N-1):
        for j in range(i+1,N):
            su=array[i]+array[j]
            if su not in sumPair:
                sumPair[su] = [i,j]
            else:
                p = sumPair[su]
                print(str(p[0])+" "+str(p[1])+" "+str(i)+" "+str(j))
                yes=True
                break
        if yes:
            break
    if yes:
        print("no pairs")
   
