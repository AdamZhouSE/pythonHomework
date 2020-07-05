list2=list(input())
list3=list(input())
list2=[int(list2[i]) for i in range(len(list2))]
list3=[int(list3[i]) for i in range(len(list3))]
list1n=0
list2n=0
def findtw(num):
    result=0
    for i in range(len(list2)):
        if i!=num:
            result+=pow(2,len(list2)-i-1)*int(list2[i])
    if list2[num]==0:
        result+=pow(2,len(list2)-num-1)*1
    return result
def findtr(num):
    result=[]
    result1=0
    for i in range(len(list3)):
        if i!=num:
            result1+=pow(3,len(list3)-i-1)*int(list3[i])
    if list3[num]==1 or list3[num]==0:
        result.append(result1+pow(3,len(list3)-num-1)*2)
    if list3[num]==1 or list3[num]==2:
        result.append(result1+pow(3,len(list3)-num-1)*0)
    if list3[num]==0 or list3[num]==2:
        result.append(result1+pow(3,len(list3)-num-1)*1)
    return result
isf=False
for i in range(len(list2)):
    for j in range(len(list3)):
        if findtw(i)==findtr(j)[0] or findtw(i)==findtr(j)[1]:
            isf=True
            print(findtw(i),end='')
            break
    if isf:
        break
            