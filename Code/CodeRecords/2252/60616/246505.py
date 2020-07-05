def equal(str1,str2):
    list1=list(str1)
    list2=list(str2)
    bo1=True
    bo2=True
    for item1 in list1:
        if(item1 not in list2):
            bo1=False
            break
        else:
            if(list1.count(item1)!=list2.count(item1)):
                bo1=False
                break
    for item2 in list2:
        if(item2 not in list1):
            bo2=False
            break
        else:
            if(list1.count(item2)!=list2.count(item2)):
                break
    return bo1 and bo2

testNum=int(input())
for i in range(testNum):
    text = input()
    string=input()
    size1=len(text)
    size2=len(string)
    ans=[]
    for j in range(size1-size2+1):
        if(equal(text[j:j+size2],string)):
            ans.append(j)
    print(len(ans))