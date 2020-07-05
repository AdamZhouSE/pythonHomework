a = int(input())
num = 0
for i in range(a+1):
    if list(str(i)).count("1")>0 :
        num += 1
print(num+1)