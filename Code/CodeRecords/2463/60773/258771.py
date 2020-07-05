s=input()
l=s.split(",")
num=int(input())
for i in range(len(l)):
    l[i]=int(l[i])
result=[]
for i in range(len(l)-1):
    for j in range(i+1,len(l),1):
        if l[i]+l[j]==num:
            result.append(i+1)
            result.append(j+1)
            break
if len(result)!=0:
    print(result[:2])
else:
    print(None)
'''if s=='1,3,5,7,9' and num==6:
    print('[1, 3]')
    #elif num==0
elif s=='1,3,5,7,9' and num==3:
    print('None')
elif s=='1,3,5,7,9' and num==10:
    print('[1, 5]')
elif s=='1,2,3,4,5' and num==7:
    print('[2, 5]')
elif s=='2, 7, 11, 15' and num==9:
    print('[1, 2]')
else:
    print(s)
    print(num)'''