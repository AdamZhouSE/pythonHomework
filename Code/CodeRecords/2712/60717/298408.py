n=int(input())
while True:
    list1=[]
    list2=[0 for i in range(0,n)]
    for i in range(0,n):
        list1.append(input())
    t=input()
    n=int(input())
    for i in range(0,len(list1)):
        for j in range(0,len(t)+1-len(list1[i])):
            if list1[i]==t[j:j+2]:
                list2[i]+=1
    print(max(list2))
    print(list1[list2.index(max(list2))])