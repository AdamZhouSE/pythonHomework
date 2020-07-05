num=int(input())
temp=input().split()
count=temp.count('5')
count0=temp.count('0')
count=int(count/9)*9
result='5' * count +'0' * count0
if result=='555555555':
    print(-1)
elif count==0 and count0==0:
    print(-1)
elif count==0 :
    print(0)
else:
    print(result)