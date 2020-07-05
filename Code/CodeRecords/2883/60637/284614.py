n,m=map(int,input().split(' '))
arr=[]
for i in range(n):
    arr.append(input().strip())
record_start=-1
record_end=-1
found_start=0
for i in range(n):
    for j in range(m):
        if(arr[i][j]=='B' and found_start==0):
            record_start=j
            found_start=1
        if(found_start==1 and arr[i][j]=='W'):
            record_end=j
            break
    if(found_start):
        if(record_end==-1):
            record_end=m
        print(i+1+(int)((record_end-record_start)/2),record_start+1+(int)((record_end-record_start)/2))
        break