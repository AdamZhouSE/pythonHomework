lines=int(input())
res=False
arr=[]
for i in range(lines):
    arr_row=list(map(int,input().split(',')))
    arr.append(arr_row)
tar=int(input())
rownum=0
for i in range(lines-1,-1,-1):
    if tar>=arr[i][0]:
        rownum=i
        break
for x in arr[rownum]:
    if x==tar:
        res=True
print(res)