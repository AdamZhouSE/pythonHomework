t=int(input())
for i in range(t):
    n=int(input())
    list=input().split(' ')
    list1=[]
    for j in range(n-1):
        if int(list[j])>int(list[j+1]):
            list1.append(int(list[j+1]))
        else:
            list1.append(int(-1))
    list1.append(-1)
    str1=''
    for s in range(len(list1)-1):
        str1=str1+str(list1[s])+' '
    str1=str1+str(list1[len(list1)-1])+' '
    print(str1)