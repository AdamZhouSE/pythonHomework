def back(num):
    num=str(num)
    for i in range(len(num)):
        if num[i]==num[len(num)-i-1]:
            if i==int((len(num)-1)/2):
                break
        else:return False
    return True
n=int(input())
m=int(input())
count=0
for i in range(n,m+1):
    if back(i):
        if pow(i,0.5).is_integer():
            if back(int(pow(i,0.5))):
                count+=1
print(count)