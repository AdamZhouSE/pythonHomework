def nums(string):
    num='0123456789'
    nums=[]
    i=0
    while i<len(string):
        midstring=''
        k=0
        for j in range(i,len(string)):
            if string[j] in num:
                midstring+=string[j]
                k=k+1
            else:
                break
        if midstring!='':
            nums.append(int(midstring))
            midstring=''
            i=i+k
        else:
            i=i+1
            continue
    return nums
n=input()
ar=input()
ar=nums(ar)
num1=ar.count(1)
num2=ar.count(2)
answer=0
if num2<=num1:
    answer=num2
    res=num1-num2
    answer+=int(res/3.0)
else:
    answer=num1
print(answer)