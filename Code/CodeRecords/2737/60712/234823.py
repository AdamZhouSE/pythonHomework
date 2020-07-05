source_list = list(map(int,input().strip("[||]").split(",")))
source_list.sort()
result = []
pre_num = source_list[0]
times = 0
i = 0
while(i<len(source_list)):
    times=times+1
    if pre_num!=source_list[i] or i ==len(source_list)-1:
        if i==len(source_list)-1:
            times = times +1
        if times-1>int(len(source_list)/3):
            result.append(pre_num)
        pre_num=source_list[i]
        times = 1
    i = i+1
print(result)
