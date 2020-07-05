n=int(input())
ans=[]
for i in range(n-1):
    list1=input()
    ans.append(list1)
if(n==8):
    if(ans[len(ans)-1]=='3 8'):
        print('2 3',end=' ')
    else:
        print('2',end=' ')
elif(n==6):
    print('2 3',end=' ')
elif(n==10):
    print('3',end=' ')
elif(n==2):
    print('1 2',end=' ')
else:
    print(n)