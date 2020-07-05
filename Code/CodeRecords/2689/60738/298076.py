n=int(input())
for i in range (n):
    string_list=list(input().split())
    str1=list(string_list[0])
    str2=list(string_list[1])
    res1=len(str1)
    res_list=[]
    for i in range(len(str2)):
        if str1.count(str2[i])>0:
            res_list.append(str1.index(str2[i]))
    res2=len(str2)-len(res_list)
    copy_list=res_list.copy()
    res_list.sort()
    for j in range(len(res_list)):
        if res_list[j]!=copy_list[j]:
            res2+=0.5
    print(int(res1+res2))
        
            
        