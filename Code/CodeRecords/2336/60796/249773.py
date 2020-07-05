n=int(input())
result=[]
while n>0:
    nums=input().split(" ")
    k=int(nums[1])
    ls=input().split(" ")
    ls=[int(x) for x in ls]
    string=""
    for i in range(0,len(ls)+1-k):
        subls=ls[i:i+k]
        m=max(subls)
        string=string+str(m)+" "
    result.append(string[:len(string)-1])
    n=n-1

for i in range(len(result)):
    print(result[i],end='')
