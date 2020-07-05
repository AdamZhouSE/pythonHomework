num=int(input())
result=0
for i in range(1,int(num/2)+1):
    if num%i==0:
        result+=i
if result == num:
    print('True')
else:
    print('False')
    