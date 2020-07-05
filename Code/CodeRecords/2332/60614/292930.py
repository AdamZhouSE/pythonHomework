num=int(input())
def judge(a):
    i=0
    while pow(num,i)<a:
        i+=1
    return min(pow(num,i)-a,a-pow(num,i-1))
def check(gap):
    i = 1
    while True:
        temp1 = pow(num, i)
        if temp1 > gap:
            temp2 = pow(num, i - 1)
            if judge(temp1 - gap) >= judge(gap - temp2):
                return [i-1,gap - temp2]
            else:
                return [i,temp1-gap]
        i+=1
target=int(input())
result=0
while target>=num:
    temp=check(target)
    result+=temp[0]
    target=temp[1]
print(result+1+(target-1)*2)