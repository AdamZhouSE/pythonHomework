a=eval(input())
a.sort()
num=fata=0
while fata!=1:
    for i in a:
        if i<num and i+1>num:
            fata=1
    num+=1
print(num)