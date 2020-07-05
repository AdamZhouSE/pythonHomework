def solve():
    pass

num=int(input())
list_ans=[]
for i in range(num):
    total=int(input())
    list_item=input()
    set_item=set(list_item)
    ans=0
    for item in set_item:
        number=list_item.count(item)
        if number%2==0:
            ans+=number
        else:
            ans+=number-1
    list_ans.append(ans)
print("\n".join(str(i) for i in list_ans))