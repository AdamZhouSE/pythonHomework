def solve():
    pass

num=int(input())
list_ans=[]
for i in range(num):
    num=input()
    ans=7-int(num)
    list_ans.append(ans)
print("\n".join(str(i) for i in list_ans))