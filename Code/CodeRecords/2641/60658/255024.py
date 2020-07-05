def add(dic,val):
    if val in dic:
        dic[val]+=1
    else:
        dic[val]=1

def remove(dic,val):
    temp = dic.pop(val)
    temp -=1
    if temp!=0:
        dic[val]=temp

s1 = input()
s2 = input()
dic1 = {}
dic2 = {}
size1 = len(s1)
for i in range(size1):
    add(dic1,s1[i])
    add(dic2,s2[i])
for i in range(size1,len(s2)):
    if dic1==dic2:
        print(True)
        exit()
    remove(dic2,s2[i-size1])
    add(dic2,s2[i])

print(dic1==dic2)