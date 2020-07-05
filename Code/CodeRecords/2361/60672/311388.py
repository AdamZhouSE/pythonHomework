from copy import copy
answer=0
def perfectsquare(num):
    n=len(num)
    answer=0
    num.sort()
    def permute(num,i):
        global answer
        if i==n:
            answer+=1
            return
        for k in range(i,n):
            if i!=k and num[i]==num[k]:
                continue
            num[i],num[k]=num[k],num[i]
            if i==0 or ((int(num[i])+int(num[i-1]))**(0.5))**2==int(num[i])+int(num[i-1]):
                permute(copy(num),i+1)
    num.sort()
    permute(num,0)
    return answer



A=list(input())
answer=perfectsquare(A)
print(answer)