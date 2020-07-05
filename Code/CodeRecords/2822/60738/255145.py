n=int(input())
num1_list=list(map(int,input().split()))
num2_list=list(map(int,input().split()))
list1=num1_list.copy()
list2=num2_list.copy()
a=num1_list[0]
b=num2_list[0]
time=0
win=0
del num1_list[0]
del num2_list[0]
def func(list1,list2):
    list1.append(list2[0])
    list1.append(list1[0])
    del list1[0]
    del list2[0]
while len(num1_list)!=0 and len(num2_list)!=0:
    if num1_list[0]>num2_list[0]:
        func(num1_list,num2_list)
    elif num1_list[0]<num2_list[0]:
        func(num2_list,num1_list)
    time+=1
    if list1==num1_list:
        time=-1
        break
if len(num1_list)==0:
    win=2
elif len(num2_list)==0:
    win=1
if win !=0:
    print(f'{time}'+" "+f'{win}')
else:
    print(-1)
    
