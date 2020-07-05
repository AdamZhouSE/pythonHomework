n = int(input())
s = ''
if(n==0):
    print("0")
else:
    
    while(n!=0):
        s += str(n%2)
        n = int(n/2)
    print(s[::-1])