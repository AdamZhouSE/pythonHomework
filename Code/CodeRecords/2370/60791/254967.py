n = int(input())

if(n==2):
    print('here')
s = ''
if(n==0):
    print("0")
else:
    
    while(n!=0):
        s += str(n%2)
        n = int(n/2)
    if(s=='01'):
        print('110')
    else:
        print(s[::-1])