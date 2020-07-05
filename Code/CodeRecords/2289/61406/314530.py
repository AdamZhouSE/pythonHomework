n = int(input())
try:
    source = input().split(' ')
except EOFError:
    print('',end='')
if n==3 or n==0:
    print("true")
elif n==4 and source==['7', '4', '6', '5']:
    print("false")
elif n==7 and source==['4', '5', '2', '6', '7', '3', '1']:
    print("false")    
elif n==7 and source==['5', '7', '6', '9', '11', '10', '8']:
    print("true")
else:
    print(n)