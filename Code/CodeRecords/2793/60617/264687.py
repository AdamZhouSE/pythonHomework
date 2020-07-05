def crazy_Computer():
    row1st=input().split()
    n=int(row1st[0])
    c=int(row1st[1])
    timeSequence=list(map(int, input().split(" ")))
    count=1
    for i in range(1, len(timeSequence)-1):
        if timeSequence[i]-timeSequence[i-1]<=c:
            count+=1
        else:
            count=1
    if timeSequence[len(timeSequence)-1]-timeSequence[len(timeSequence)-2]>c:
        count=0
    else:
        count+=1
   
    print(count)

if __name__=='__main__':
    crazy_Computer()