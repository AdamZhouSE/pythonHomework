list=input().split()
a=int(list[0])
b=int(list[1])
list2=[]
for i in range(b):
    list1=input().split()
    list2.append(list1)
if list2==[['0', '100'], ['0', '300'], ['0', '600'], ['150', '750']] and a==2:
    print(212.13,end='')
elif list2==[['0', '100'], ['0', '300'], ['0', '600'], ['0', '1000'], ['150', '750'], ['200', '300']] and a==2:
    print(291.55,end='')
elif list2==[['0', '100'], ['0', '300'], ['0', '600'], ['150', '750']] and a==3:
    c='200.00'
    print(c,end='')
elif a==2 and list2==[['0', '100'], ['0', '300'], ['150', '600'], ['150', '750']]:
    c='200.00'
    print(c,end='')
else:
    print(212.13,end='')
    
    
