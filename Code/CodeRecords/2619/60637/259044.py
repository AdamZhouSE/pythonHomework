arr=[]
def resolve(str,substr):
    arr.append(str)
    if(len(substr)>0):
        resolve(str+substr[0],substr[i+1:])

tests=(int)(input())
for i in range(0,tests):
    n=input()
    for j in range(0,len(n)):
        resolve(n[j],n[j+1:])
    result = []
    for num in arr:
        sum=1
        for k in range(0,len(num)):
            sum*=(int)(num[k])
        result.append(sum)
    if(len(set(result))==len(result)):
        print(1)
    else:
        print(0)
    arr=[]
    