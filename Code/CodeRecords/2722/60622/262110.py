def solve():
    pass

num=int(input())
list_ans=[]
for i in range(num):
    num=input()
    if num[-1:]=='0' or num[-1:]=='5':
        list_ans.append("YES")
    else:
        list_ans.append("NO")
print("\n".join(str(i) for i in list_ans))
