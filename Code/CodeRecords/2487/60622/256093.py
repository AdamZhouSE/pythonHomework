def solve(list_name):
    arr=[]
    set_name=set(list_name)
    for name in set_name:
        num=list_name.count(name)
        arr.append((num,name))
    arr.sort(key=lambda s:(-s[0],s[1]))
    tuple_name=arr[0]
    str_ans=str(tuple_name[1])+" "+str(tuple_name[0])
    return str_ans

n=int(input())
list_ans=[]
for i in  range(n):
    list_len=int(input())
    list_candicate=input().split()
    ans=solve(list_candicate)
    list_ans.append(ans)
print("\n".join(str(i) for i in list_ans))
