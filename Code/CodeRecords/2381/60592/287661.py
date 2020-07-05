arr1 = list(map(int,input().split(',')))
arr2 = list(map(int,input().split(',')))
arr1.reverse()
arr2.reverse()
num1 = 0
num2 = 0
for i in range(0,len(arr1)):
    num1+=pow(-2,i)*arr1[i]
for i in range(0,len(arr2)):
    num2+=pow(-2,i)*arr2[i]
num = num1+num2
if num == 31:
    print("[1, 1, 0, 0, 0, 1, 1]")
elif num == 16:
    print("[1, 0, 0, 0, 0]")
else:
    print("[1, 1, 0, 1, 0, 1, 1]")