def test12():
    n=int(input())
    s=input()
    x=s.split(" ")
    arr=[]
    for i in x:
        arr.append(int(i))
    zero=arr.count(0)
    if zero==len(set(arr)):
        print(s)
        return 0
    return len(set(arr))
print(test12())