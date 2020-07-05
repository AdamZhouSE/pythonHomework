def solve():
    pass

num=int(input())
list_ans=[]
for i in range(num):
    arr_len=int(input())
    arr=list(map(int,input().split()))
    max=0
    for m in range(arr_len):
        for n in range(m+1,arr_len):
            if min(arr[m],arr[n])*(n-m)>max:
                max=min(arr[m], arr[n]) * (n - m)
    print(max)
print("\n".join(str(i) for i in list_ans))