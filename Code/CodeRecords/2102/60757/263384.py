
def judge(num):
    for i in range(2,num):
        if num%i ==0:
            return '1'
    return '0'
n=int(input())
count=0
for i in range(2,n+1):
    if judge(i)=='0':
        count=count+1
print(count)
