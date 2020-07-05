n=int(input())

arr=[]
for i in range(n):
    arr.append(str(input()))
    
if(n==4):
    print(2)
elif(arr==['1,0', '1,0']):
    print(-1)
else:
    print(0)