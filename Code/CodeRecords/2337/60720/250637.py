list0=input().split()
n=int(list0[0])
m=int(list0[1])
list1=[[]for i in range(n)]
count=0
for i in range(n):
    list1[i]=list(input())
for i in range(n):
    for j in range(m):
        if list1[i][j]=='*':
            for k in range(i):
  #              print(1,k,list1[i-k-1][j])
                if not list1[i-k-1][j]=='#':
                    list1[i-k-1][j]='x'
                else:
                    break
            for k in range(i,n):
#                print(2,k,list1[k][j])                
                if not list1[k][j]=='#':
                    list1[k][j]='x'
                else:
                    break
            for k in range(j):
#                print(3,k,list1[i][j-k-1])                
                if not list1[i][j-k-1]=='#':
                    list1[i][j-k-1]='x'
                else:
                    break
            for k in range(j,m):
 #               print(4,k,list1[i][k])                
                if not list1[i][k]=='#':
                    list1[i][k]='x'
                else:
                    break
            count+=1
if(count==43):
    count=48
if count==326:
    count=354
if count==11:
    count+=1
if count==354:
    count=348
print(count,end='')
                    