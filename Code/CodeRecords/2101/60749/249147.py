def judgehappynumber(num):
    num_str=str(num)
    num_array=[]
    for x in num_str:
        num_array.append(int(x))
    count=0
    sum=0
    while True:

        for x in num_array:
            sum+=x*x
        count+=1
        if sum==1:
            return True
        if count>10000:
            return False
        num=str(sum)
        num_array=[]
        for h in num:
            num_array.append(int(h))
        sum=0
n=int(input())
print(judgehappynumber(n))