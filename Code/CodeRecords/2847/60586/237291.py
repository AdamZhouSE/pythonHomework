def test13():
    n=int(input())
    d=input().split(" ")
    di=[]
    for item in d:
        di.append(int(item))
    x=input().split(" ")
    a=int(x[0])
    b=int(x[1])
    sum=0
    for i in range(b-a):
        sum=sum+di[i+a-1]
    return sum
print(test13())