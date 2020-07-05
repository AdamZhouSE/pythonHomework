a = int(input())
count = 0
for i in range(a):
    count+=(''+str(i+1)).count('1')
print(count)