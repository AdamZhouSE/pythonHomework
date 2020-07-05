k = int(input())
n = int(input())
count = 0
while True:
    if 2**count>n:
        break
    else:
        count+=1
print(count)