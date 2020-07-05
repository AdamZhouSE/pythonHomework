def cut(str1,str2):
    while str2 in str1:
        for i in range(0,len(str1)):
            if str1[i:i+len(str2)]==str2:
                str1=str1[:i]+str1[i+len(str2):]
    return str1

list1=eval(input())
list2=[]
for i in list1:
    tmp1=[i]
    for j in range(0,len(list1)):
        tmp2=[]
        for k in tmp1:
            if list1[j] in k and i!=list1[j]:
                tmp2.append(cut(k,list1[j]))
        tmp1+=tmp2
    for j in tmp1:
        if j!=i and j in list1:
            list2.append(i)
            break
print(list2)