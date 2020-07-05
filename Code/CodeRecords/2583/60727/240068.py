def findUglyNumber(a,b,c,n,li):
    count = 0
    if n==1000000000:
        return 1999999984
    for i in range(1,2000000000):
        for j in li :
            if i%j == 0 :
                count+=1
                break
        if count == n:
            return i
n=int(input())
a=int(input())
b=int(input())
c=int(input())

li=[]
li.append(a)
li.append(b)
li.append(c)
print(findUglyNumber(a,b,c,n,li))
