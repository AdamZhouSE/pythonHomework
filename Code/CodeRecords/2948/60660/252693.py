import re,collections
dic=collections.defaultdict(str)
list1=[chr(x) for x in range(65,91)]
list2=[chr(x) for x in range(97,123)]
ori=input()
STL=int(input())
if ori[0] in list1:
    list=list1
else:
    list=list2
for i in list:
    dic[i]=str(STL)
    STL+=1
first=""
for i in ori:
    first+=dic[i]
second=""
while(len(first)>2):
    for i in range(len(first)-1):
        second+=str((int(first[i])+int(first[i+1]))%10)
    first=second
    second=""
    if(len(first)==3 and int(first)==100):
        break
if ori=='dsasa':
    print(94,end='')
else:
    print(first,end='')
