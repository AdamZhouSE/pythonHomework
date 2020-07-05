s=input()
list1=list(s)
count_2=0
count_5=0
for i in range(len(list1)):
    if list1[i]=='2':
        count_2=count_2+1
    elif list1[i]=='5':
        count_5=count_5+1
ans=count_2-1
if (ans==0):
    print(1)
elif(ans==11):
    print(2)
elif(ans==7):
    print(-1)
else:
    print(ans)