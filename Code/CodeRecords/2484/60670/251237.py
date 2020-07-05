t=int(input())
for i in range(0,t):
    tmp=input().split(' ')
    n=int(tmp[0])
    m=int(tmp[1])
    arr_a=input().split(' ')
    arr_b=input().split(' ')
    arr=[]
    for j in arr_a:
        if not (j in arr):
            arr.append(j)
    for j in arr_b:
        if not(j in arr):
            arr.append(j)
    print(len(arr))