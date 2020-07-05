list=input()
#如果从这个数开始，每一个数都比前一个大， 则加一
def num(a,list):
    for i in range(len(list)):
        if int(list[i])<int(a):
            return False
    return True
max=0
list1=[]
res=1
for i in range(len(list)):
    if int(list[i])>=max:
        if i==len(list)-1:
            res+=1
        else:
            max=int(list[i])
            list1=[]
            for j in range(i,len(list)):
                list1.append(list[j])
            if num(max,list1):
                res+=1
print(res)
