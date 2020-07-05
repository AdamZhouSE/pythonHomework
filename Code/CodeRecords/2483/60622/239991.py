def solve(str,patt):
    patt_set=set(patt)
    ans="$"
    index=len(str)
    for p in patt_set:
        if ((str.find(p)!=-1)and(str.find(p)<index)):
            index=str.find(p)
    if index!=len(str):
        ans=str[index]
    return ans


num=int(input())
list_ans=[]
for i in range(num):
    Str=input()
    Patt=input()
    ans=solve(Str,Patt)
    list_ans.append(ans)
print("\n".join(str(i) for i in list_ans))
