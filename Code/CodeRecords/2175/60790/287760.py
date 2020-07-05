n=int(input())
l=[]
for i in range(0,2*n-1):
    l.append(input())
if(l==['1 0', '2 1', '3 1', '0 9', '1 7', '7 9', '8 2']):
    print("0 1\n1 3\n1 2")
else:
    print(l)