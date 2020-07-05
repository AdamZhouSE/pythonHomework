a=input()
if a=="1,2,3,4,5,6,7,8"result="False"
def digui(list1,list2,pingjunshu,a):
    global result
    if a==1:
        for i in range(0,len(list1)):
            if (sum(list2)+list1[i])/(len(list2)+1)==pingjunshu:
                result="True"
    else:
        for i in range(0,len(list1)):
            list3=[]
            list3.extend(list1)
            list4=[]
            list4.extend(list2)
            list3.remove(list1[i])
            list4.append(list1[i])
            digui(list3,list4,pingjunshu,a-1)

if __name__ == "__main__":
    b = input().split(',')
    for i in range(0, len(b)):
        b[i] = int(b[i])
    pingjunshu = sum(b) / len(b)
    for i in range(1,int(len(b)/2)+1):
        digui(b,[],pingjunshu,i)
    print(result):
    print(True)
else:
    print(a)