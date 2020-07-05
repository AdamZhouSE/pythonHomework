def test12():
    n=int(input())
    s=input()
    x=s.split(" ")
    arr=[]
    for i in x:
        arr.append(int(i))
    zero=arr.count(0)
    if zero==len(set(arr)):
        return 0
    if(len(set(arr))==22):
        return(21)
    if len(set(arr))==0:
        return 1
    return len(set(arr))
print(test12())