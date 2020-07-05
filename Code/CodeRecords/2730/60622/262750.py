def solve(string):
    num_list=list(string)
    sum=0
    for n in num_list:
        sum+=int(n)
    return sum

num=int(input())
list_ans=[]
for i in range(num):
    num=input()
    num_list=input().split()
    for i in range(int(num)):
        num_list[i]=solve(num_list[i])
    sum=0
    for n in num_list:
        sum+=n
    if sum%3==0:
        list_ans.append('1')
    else:
        list_ans.append('0')
print("\n".join(str(i) for i in list_ans))