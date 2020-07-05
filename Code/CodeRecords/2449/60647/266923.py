list1=input()
n=int(input())
list=[]
for i in list1:
    if i!='['and i!=']'and i!=',':
        list.append(int(i))
b=0
if n not in list:
    print('-1')
else:
    for i in range(len(list)-1):
        if n==int(list[i]):
            print(i)
