def solve():
    pass

num=int(input())
list_ans=[]
for i in range(num):
    tem=input().split()
    A=int(tem[0])
    B=int(tem[1])
    C=int(tem[2])
    list_ans.append(pow(A,B)%C)
print("\n".join(str(i) for i in list_ans))