n,m=map(int,input().strip().split(" "))
arr=list(map(int,input().strip().split(" ")))
for i in range(m):
    order=list(map(str,input().strip().split(" ")))
    if order[0]=="Q":
        left,right,k=map(int,order[1:])
        print(sorted(arr[left-1:right])[k-1])
    elif order[0]=="C":
        idx,value=map(int,order[1:])
        arr[idx-1]=value