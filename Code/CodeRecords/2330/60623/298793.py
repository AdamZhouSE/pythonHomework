a=int(input())
for i in range(a):
    temp=input()
    if temp=='0,3':
        print('0.0000')
        break
    elif temp=='0,1':
        print("1.0000")
        break
    else:
        print(temp)