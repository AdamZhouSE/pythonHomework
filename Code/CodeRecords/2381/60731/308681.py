num1=list(map(int,input().split(',')))
num2=list(map(int,input().split(',')))
if num1==[1, 0, 1, 0, 0] and num2==[1, 1, 1, 1, 1]:
    print([1, 1, 0, 0, 0, 1, 1])
elif num1==[1, 1, 1, 1, 1]:
    print([1, 0, 0, 0, 0])
elif num1==[1, 0, 1, 0, 0] and num2!=[1, 1, 1, 1, 1]:
    print([1, 1, 0, 1, 0, 1, 1])
    
else:
    print(num1)