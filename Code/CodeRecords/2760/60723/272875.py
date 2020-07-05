num=int(input())
for i in range(num):
    temp=input().split()
    number=int(temp[0])
    money=int(temp[1])
    print(int((number+1)/2)*money)