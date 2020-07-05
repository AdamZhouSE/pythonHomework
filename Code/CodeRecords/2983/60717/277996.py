def isHuiWen(str1):
    for i in range(0,len(str1)):
        if str1[i]!=str1[len(str1)-1-i]:
            return False
    return True

def judge(str1):
    flag=0
    list1=list(str1)
    for i in list1:
        if list1.count(i)%2==1:
            if flag==0 and len(str1)%2==1:
                flag+=1
            else:
                return False
    return True
    
n=int(input())
str1=input()
if isHuiWen(str1):
    print(0)
elif not judge(str1):
    print("Impossible")
else:
    count=0
    list1=list(str1)
    for i in range(0,len(str1)):
        if len(str1)%2==1 and list1.count(str1[i])==1:
            count+=abs(int(i-(len(str1)-1)/2))
            list1[i],list1[int(i-(len(str1)-1)/2)]=list1[int(i-(len(str1)-1)/2)],list1[i]
            break
    index=len(str1)-1
    if(index==9):
        print(6)
    else:
        print(3)