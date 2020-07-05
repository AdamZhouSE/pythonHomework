
num=int(input());
list_ans=[]
for i in range(num):
    n, m = input().split()
    arr_n=set(input().split())
    arr_m=set(input().split())
    set_ans=arr_m|arr_n
    list_ans.append(len(set_ans))
print("\n".join(str(i) for i in list_ans))