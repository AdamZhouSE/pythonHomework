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
nm=input()
nm=nums(nm)
n,m=nm[0],nm[1]
ar=nums(input())
print(ar)
for i in range(m):
    lr=nums(input())
    print(lr)
    l,r=lr[0],lr[1]
    if l==r:
        print(10)
    else:
        length=r-l+1
        if length%2!=0:
            print(20)
        else:
            num1=ar.count(1)
            num2=ar.count(-1)
            print(num1)
            print(num2)
            if num1>=int(length/2.0) and num2>=int(length/2.0):
                print(1)
            else:
                print(30)