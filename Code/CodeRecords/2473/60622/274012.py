def solve():
    print(arr[0])
    pass

num=int(input())
list_ans=[]
S_list=[]
for i in range(num):
    arr_len=int(input())
    arr=list(map(int,input().split()))
    for i in range(arr_len):
        p,q=i-1,i+1
        while p>=0 and arr[p]>=arr[i]:
            p-=1
        while q<=arr_len-1 and arr[q]>=arr[i]:
            q+=1
        S=(q-p+1-2)*arr[i]
        S_list.append(S)
    S_list.sort()
    list_ans.append(S_list.pop())
    S_list=[]
print("\n".join(str(i) for i in list_ans))

