n = int(input())
count = 1
for i in range(0,n+1):
    if str(i).find('1')!=-1:
        count+=1
print(count)