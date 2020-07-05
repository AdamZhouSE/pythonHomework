list=input()[1:-1]
list=list.split(',')
for i in range(len(list)):
    list[i]=int(list[i])
list.sort()
print('[',end="")
for i in range(len(list)-1):
    print(list[i],", ",sep="",end="")
print(list[-1],"]",sep="")