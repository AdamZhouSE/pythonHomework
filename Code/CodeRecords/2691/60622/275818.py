def solve(arr):
    s=0
    for num in arr:
        s+=num
    sum=s//2
    table=[]
    for i in range(len(arr)+1):
        table.append([0]*(sum+1))
    for i in range(len(table[0])):
        table[0][i]=0
    for i in range(len(arr)+1):
        table[i][0]=0
    for i in range(1,len(arr)+1):
        for j in range(1,sum+1):
            if(j-arr[i-1]>=0):
                x=table[i - 1][j]
                y=table[i-1][j-arr[i-1]]+arr[i-1]
                table[i][j]=max(table[i-1][j],table[i-1][j-arr[i-1]]+arr[i-1])
            else:
                table[i][j]=table[i-1][j]

    return s-2*table[-1][-1]

num=int(input())
list_ans=[]
for i in range(num):
    arr_len=int(input())
    arr=list(map(int,input().split()))
    ans=solve(arr)
    list_ans.append(ans)
print("\n".join(str(i) for i in list_ans))




