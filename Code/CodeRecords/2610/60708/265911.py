N=int(input())
for n in range(0,N):
    result=0
    l=int(input())
    temp=input().split(" ")
    str="".join(temp)

    for i in range(1,l+1):
        list1=[]
        for j in range(0,l-i+1):
            list1.append(str[j:j+i])
        for item in list1:
            list2=list(item)
            list3=set(list2)
            if(len(list3)==len(list2)):
                result=result+len(list2)
    print(result)