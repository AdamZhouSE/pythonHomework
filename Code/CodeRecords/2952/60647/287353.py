str=input()
n=int(input())
list=[]
temp=[]
for i in range(len(str)):
    if str[i]=='P':
        k=[]
        for j in temp:
            k.append(j)
        list.append(k)
    elif str[i]=='B':
        temp.pop()
    else:
        temp.append(str[i])
def count(str1,str2):
    res=0
    for i in range(len(str2)-len(str1)+1):
        if str1[0]==str2[i]:
            a=0
            for j in range(i,i+len(str1)):
                if str2[j]!=str1[j-i]:
                    a=1
                    break
            if a==0:
                res+=1
    return res

for i in range(n):
    list1=input().split()
    a=int(list1[0])-1
    b=int(list1[1])-1
    str1=list[a]
    str2=list[b]
    print(count(str1,str2))