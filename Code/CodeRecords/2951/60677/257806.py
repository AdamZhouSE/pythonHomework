def trans2(num):
    num=list(str(num))
    num.reverse()
    n=num.__len__()
    answer=0
    for i in range(n):
        answer+=int(num[i])*(2**i)
    return answer

def trans3(num):
    num=list(str(num))
    num.reverse()
    n=num.__len__()
    answer=0
    for i in range(n):
        answer+=int(num[i])*(3**i)
    return answer
list2=list(input())
list3=list(input())
list22=[]
list33=[]
for i in range(list2.__len__()):
    list2=[int(x) for x in list2]
    list2[i]=(list2[i]+1)%2
    list2=[str(x) for x in list2]
    list22.append("".join(list2))
    list2=[int(x) for x in list2]
    list2[i]=(list2[i]+1)%2
    i=i+1
for i in range(list3.__len__()):
    list3=[int(x) for x in list3]
    list3[i]=(list3[i]+1)%3
    list3=[str(x) for x in list3]
    list33.append("".join(list3))
    list3=[int(x) for x in list3]
    list3[i]=(list3[i]+1)%3
    list3=[str(x) for x in list3]
    list33.append("".join(list3))
    list3=[int(x) for x in list3]
    list3[i]=(list3[i]+1)%3
    i=i+1

for i in list22:
    for j in list33:
        if trans2(i)==trans3((j)):
            print(trans2(i),end="")
            break