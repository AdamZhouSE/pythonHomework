def solve(bin):
    num0=int("0b"+bin[0],2)
    num1= int("0b" + bin[1], 2)
    return  num0*num1

num=int(input())
list_ans=[]
for i in range(num):
    list_bin=input().split()
    ans=solve(list_bin)
    list_ans.append(ans)
print("\n".join(str(i) for i in list_ans))
