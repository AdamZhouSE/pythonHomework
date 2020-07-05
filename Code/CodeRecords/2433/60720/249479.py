list1=eval(input())
def iso(listm):
    for i in range(len(listm)):
        for j in range(i+1,len(listm)):
            if listm[i][1]>=listm[j][0]:
                return True
    return False
while iso(list1):
    isF=False
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i][1]>=list1[j][0]:
                list1[i][1]=list1[j][1]
                del list1[j]
                isF=True
                break
        if isF:
            break
print(list1)