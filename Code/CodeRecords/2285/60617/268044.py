def shares_trade():
    T=int(input())
    for i in range(0, T):
        N=int(input())
        arr=list(map(int, input().split(" ")))
        maxProfit(N, arr)

def maxProfit(N, arr):
    stack=[]
    res=[]
    if N==1:
        return 0
    flag=True
    for i in range(0, N-1):
        if arr[i+1]>arr[i]:
            flag=False
            break
    if flag:
        return ""
    else:
        for i in range(0, N):
            if not stack:
                stack.append(i)
            else:
                if arr[i]>arr[stack[-1]]:
                    if len(stack)>=2:
                        stack.pop()
                        stack.append(i)
                    else:
                        stack.append(i)
                else:
                    if len(stack)==1:
                        stack.pop()
                        stack.append(i)
                    else:
                        sold=stack.pop()
                        buy=stack.pop()
                        res.append([buy, sold])
                        stack.append(i)
    if len(stack)==2:
        sold=stack.pop()
        buy=stack.pop()
        res.append([buy, sold])

    for ele in res:
        print("("+str(ele[0])+" "+str(ele[1])+")"+" ", end="")
    print()

if __name__=='__main__':
    shares_trade()