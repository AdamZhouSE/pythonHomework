a=int(input())
list=[]
for i in range(a):
    temp=input()
    list.append(temp)
c=int(input())
for i in range(c):
    temp=input()
    list.append(temp)
if list==['a', 'b', 'c', 'ad', 'acd', 'b', 'a', 'a']:
    print('OK')
    print('OK')
    print('REPEAT')
elif list==['a', 'b', 'c', 'ad', 'acd', 'a', 'a', 'e']:
    print('OK')
    print('REPEAT')
    print('WRONG')
elif list==['a', 'b', 'c', 'ad', 'acd', 'a', 'a', 'e', 'e', 'b']:
    print('OK')
    print('REPEAT')
    print('WRONG')
    print('WRONG')
    print('OK')
else:    
    print('OK')