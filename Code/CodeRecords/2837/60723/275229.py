temp=input().split()
n=int(temp[0])
l=int(temp[1])
r=int(temp[2])
def min_result(n,l,r):
    max_num=n-l
    count=0
    for i in range(l):
        count=count+int(pow(2,i))
    count=count+max_num
    return count
def max_result(n,l,r):
    min_num=n-r
    count=0
    for i in range(r):
        count=count+int(pow(2,i))
    count=count+min_num*int(pow(2,r-1))
    return count
print(str(min_result(n,l,r))+' '+str(max_result(n,l,r)))