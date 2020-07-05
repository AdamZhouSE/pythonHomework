method=0
n=input()
list=input().split(" ")
for num in range(600):
    if str(num+1) in list:
        method+=1
print(method)