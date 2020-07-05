def solution():
    n=int(input())
    arr=input().split(' ')
    s=''
    for i in range(n):
        s=s+arr[i]
    miss=[]
    repeat=[]
    for i in range(1,n+1):
        if str(i) not in arr:
            miss.append(i)
        elif s.count(str(i)) > 1:
            repeat.append(i)
        else:
            continue
    b=''
    a=''
    if len(repeat)==0:
        b='0'
    elif len(repeat)==1:
        b=str(repeat[0])
    else:
        b=str(min(repeat))
    if len(miss)==0:
        a='0'
    elif len(miss)==1:
        a=str(miss[0])
    else:
        a=str(min(miss))
    result=b+' '+a
    print(result)


def main():
    T=int(input())
    for i in range(T):
        solution()

main()

