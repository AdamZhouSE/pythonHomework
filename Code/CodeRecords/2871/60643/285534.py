def solution(data):
    cnt=0
    num1=data.count(1)
    num2=data.count(2)
    if num1<=num2:
        cnt=num1
    else:
        cnt=num2+(num1-num2)//3
    return cnt

if __name__=="__main__":
    n=int(input())
    data = input().split()
    data = [int(x) for x in data]
    ans = solution(data)
    print(ans)