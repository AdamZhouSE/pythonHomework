n=int(input())
max=0
s_list=[]
for i in range(0,n):
    s_list.append(input())
for i in range(1,len(s_list[0])+1):
    # i 表示字符串長度
    for j in range(0,len(s_list[0])-i+1):
        # j 表示子串起始位置
        all_contain=True
        for k in range(1,len(s_list)):
            if s_list[0][j:j+i] not in s_list[k]:
                all_contain=False
                break
        if(all_contain):
            if i>max:
                max=i
print(max)