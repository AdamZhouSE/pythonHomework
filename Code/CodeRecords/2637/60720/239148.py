list1=eval(input())
for i in range(len(list1)):
    isT=True
    for j in range(i):
        if(list1[i]<=list1[j]):
            isT=False
            break
    for j in range(i+1,len(list1)):
        if(list1[i]<=list1[j]):
            isT=False
            break
    if isT==True:
        print(i)