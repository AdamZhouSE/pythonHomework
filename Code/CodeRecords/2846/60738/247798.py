n=int(input())
num_list=list(map(int,input().split(" ")))
differ_list=[]
for i in range(n):
    if num_list[i]!=0:
        if num_list[i] not in differ_list:
            differ_list.append(num_list[i])
print(len(differ_list))