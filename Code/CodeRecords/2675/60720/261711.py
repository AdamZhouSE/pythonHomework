size=int(input())
for i in range(size):
    list1=list(input())
    list1=[int(list1[j]) for j in range(len(list1))]
    a=0
    b=0
    for i in range(len(list1)):
        if list1[i]==6:
            a+=9*pow(10,(len(list1)-i-1))
        else:
            a+=list1[i]*pow(10,(len(list1)-i-1))
        b+=list1[i]*pow(10,(len(list1)-i-1))
    print(a-b)
        