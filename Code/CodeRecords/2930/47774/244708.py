number=eval(input())
string=input()
num=[int(n) for n in string.split()]
index=0
for i in range(1,number-1):
    if(num[i]<num[i-1] and num[i]<num[i+1]):
        index=index+1
    if(num[i]>num[i-1] and num[i]>num[i+1]):
        index=index+1
print(index)