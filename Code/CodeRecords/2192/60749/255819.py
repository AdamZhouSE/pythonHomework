n=int(input())
num_array=[]
for h in range(n):
    num_array.append(int(input()))
def create_array(n):
    temp=n
    res=[]
    res.append(n)
    while n>0:
        n=n-5
        res.append(n)



    while not n==temp:
        n=n+5
        res.append(n)
    strresult=str(res[0])
    for n in range(1,len(res)):
        strresult=strresult+" "+str(res[n])
    return strresult
for _ in range(0,len(num_array)):
    print(create_array(num_array[_]))