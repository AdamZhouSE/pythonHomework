#处理输入
lst = list(map(int,input().split(',')))

#法一 暴力解
maxSum = lst[0]
for i in range(len(lst)):#begin
    for j in range(i+1,len(lst)+1):#end
        maxSum = max(sum(lst[i:j]),maxSum)
print(maxSum)