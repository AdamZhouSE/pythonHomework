list1=input().split(',')
for i in range(len(list1)):
    list1[i]=int(list1[i])
list1.sort()
l=len(list1)
cl=1
for i in range(l-1):
    if list1[i]==list1[i+1]:
        cl+=1
    else:
        break
isN=True
if l%cl==0 and not cl==1:
    for i in range(cl,l-cl,cl):
        for j in range(0,cl):
            if list1[i+j]!=list1[i+j]:
                isN=False
                break
    if isN:
        print('True')
    else:
        print('False')
else:
    print('False')

        