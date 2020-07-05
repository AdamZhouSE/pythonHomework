list1=input().split(',')
list2=input().split(',')
list1=[int(list1[i]) for i in range(len(list1))]
list2=[int(list2[i]) for i in range(len(list2))]
isE=True
for i in range(2):
    if ((list1[0]>list2[2*i]) and ( list1[1]>list2[2*i+1]) and (list1[2]<list2[2*i]) and (list1[3]<list2[2*i+1])) or ((list1[0]<list2[2*i]) and (list1[1]<list2[2*i+1]) and (list1[2]>list2[2*i]) and( list1[3]>list2[2*i+1])):
        print('True')
        isE=False
        break
if isE:
    print('False')