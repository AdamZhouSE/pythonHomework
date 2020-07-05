n=int(input())
num1=list()
for a in range(0,n):
    mid=eval("["+input()+"]")
    num1.append(list(int(i) for i in mid))
k=int(input())
num2=list()
for a in range(len(num1)):
    num2.extend(num1[a])
num2=sorted(num2)
print(num2[k-1])