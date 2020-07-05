nlr = list(map(int,input().split()))
min = 0
max = 0
temp =1
for i in range(nlr[0]):
    if i < nlr[1]:
        min = min +temp
        temp =temp*2
    else:
        min = min +1
temp=1
for i in range(nlr[0]):
    if i <nlr[2]:
        max = max+temp
        temp=temp*2
    else:
        
        max = max+int(temp/2)
print(min,max)