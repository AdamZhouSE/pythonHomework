m=int(input())
n=int(input())
nums=int(input())
[row_min,col_min]=[m,n]
for i in range(0,nums):
    temp=list(map(int,input().split(",")))
    row_min=min(row_min,temp[0])
    col_min=min(col_min,temp[1])
print(row_min*col_min)