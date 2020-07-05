num = int(input())
str1 = str(sorted(input().strip()))

for i in range (num-1) :
    s = str(sorted(input().strip()))
    str1 =  str1+"."+s
str2 = str1.split(".")
str3 = sorted(str2)

count0 = 1
for i in range (num-1):
    if str3[i].__eq__(str3[i+1]) :
        continue
    else:
        count0= count0+1
print(count0,end='')
