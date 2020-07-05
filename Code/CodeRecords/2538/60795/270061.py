arr=eval(input())
arr.sort()
num=1
while True:
    if num in arr:
        num+=1
    else:
        break
    
print(num)