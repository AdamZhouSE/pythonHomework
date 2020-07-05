n=int(input())

list1=[]

for i in range(1,int((n+1)/2)):
    tmp=(2*i-1)*'D'
    tmp=tmp+(int((n+1)/2)-i)*'*'
    tmp=(int((n+1)/2)-i)*'*'+tmp
    list1.append(tmp)

for i in range(0,int((n+1)/2)-1):
    print(list1[i])

print(n*'D')

for i in range(0,int((n+1)/2)-1):
    print(list1[len(list1)-1-i])
   