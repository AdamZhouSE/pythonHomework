def solve():
    pass

num=int(input())
list_ans=[]
for i in range(num):
    n=int(input())
    count=0
    for i in range(1,n+1):
        count+=i*i
    list_ans.append(count)
    pass
print("\n".join(str(i) for i in list_ans))