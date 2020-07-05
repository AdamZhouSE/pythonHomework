def test12():
    n=int(input())
    x=input().split(" ")
    arr=[]
    for i in x:
        arr.append(int(i))
    zero=arr.count(0)
    return len(set(arr))-zero
print(test12())