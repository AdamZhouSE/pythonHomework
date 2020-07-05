def crazy_Computer():
    row1st=input().split()
    n=int(row1st[0])
    c=int(row1st[1])
    timeSequence=list(map(int, input().split(" ")))
    count=0
    for i in range(1, len(timeSequence)):
        if timeSequence[i]-timeSequence[i-1]<=c:
            count+=1
        else:
            count=0
    print(count)
    
if __name__=='__main__':
    crazy_Computer()
