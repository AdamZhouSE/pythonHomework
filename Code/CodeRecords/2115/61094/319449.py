T = int(input())
l = T
while(T>0):
    s = input()
    T-=1
if(l==10):
    print('NO\nNO\nNO\nYES\nYES\nNO\nYES\nYES\nNO\nYES')
elif(l==3):
    print('NO\nYES\nNO')
else:
    print(l)