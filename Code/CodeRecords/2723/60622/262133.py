def solve(num):
    set_num=set(num)
    sum=0
    for n in set_num:
        sum+=int(n)
    return  str(sum)

num=int(input())
list_ans=[]
for i in range(num):
    num=input()
    while len(num)!=1:
        num=solve(num)
    list_ans.append(num)
print("\n".join(str(i) for i in list_ans))
