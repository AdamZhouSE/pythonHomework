num=int(input())
list_ans=[]
for i in range(num):
    x=int(input())
    if x%2==0:
        list_ans.append("Player B")
    else:
        list_ans.append("Player A")
print("\n".join(str(i) for i in list_ans))
