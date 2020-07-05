n=int(input())
str_list=[]
for i in range(n):
    str1=str(input())
    str1="".join(sorted(str1))
    str_list.append(str1)
str_list.sort()
res=1
for i in range(1,len(str_list)):
    if str_list[i]!=str_list[i-1]:
        res+=1
print(res,end="")