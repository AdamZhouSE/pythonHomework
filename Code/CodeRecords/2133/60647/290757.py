list=input().split(',')
for i in range(len(list)):
    list[i]=int(list[i])
list.sort()
def xiangdeng(list):
    for i in range(len(list)-1):
        if int(list[i])!=int(list[i+1]):
            return False
    return True
a=0
while not xiangdeng(list):
    for i in range(len(list)-1):
        list[i]=int(list[i])+1
    list.sort()
    a+=1
print(a)