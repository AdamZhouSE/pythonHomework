num_str=input();
dightLastIndex=[None for _ in range(10)];
#统计每个数字最后出现的索引
for i,digit in enumerate(num_str):
    dightLastIndex[int(digit)]=i;
res="";
for i,digit in enumerate(num_str):
    for index in range(9,int(digit),-1):
        if dightLastIndex[index]!=None and dightLastIndex[index] > i:# i 位置的元素和digit_last_index[index] 交换
            res=num_str[: i] + num_str[dightLastIndex[index]] + num_str[i + 1: dightLastIndex[index]] + num_str[i] + num_str[dightLastIndex[index] + 1:]
print(res);