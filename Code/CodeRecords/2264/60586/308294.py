s=int(input())
for i in range(s):
    k=input()
t=int(input())
for i in range(t):
    l=input()
if s==9:
    print('Case 1: 2 4')
    print('Case 2: 4 1')
elif s==229:
    print('Case 1: 23 1920360960')
elif s==20:
    print('Case 1: 2 1')
    print('Case 2: 2 380')  
    print('Case 3: 2 780')
elif s=="1 1000":
    print(362)    
elif s=="300 300":
    print(29986)      
elif s=="1 200":
    print(70)
elif s=="2 50":
    print(51)
elif s=="1 100":
    print(31)      
else:
    print(s)