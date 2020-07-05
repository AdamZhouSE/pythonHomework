NUM=int(input())
lst=[int(input()) for i in range(NUM)]
result=0
for i in range(1,NUM):
    result+=max(lst[i-1],lst[i])
print(result)