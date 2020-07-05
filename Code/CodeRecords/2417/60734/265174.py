lst = list(map(int,input().split(',')))
max_n = min(lst)
flag = True
for i in range(2,max_n+1):
    count = 0
    for index in range(len(lst)):
        if lst[index]%i == 0:
            count+=1
    if count==len(lst):
        flag = False
        break
print(flag)