def Tanya_climbStairs():
    n=int(input())
    shout=list(map(int, input().split(" ")))
    stairs=[]
    for i in range(0, len(shout)):
        if i==len(shout)-1:
            stairs.append(shout[len(shout)-1])
        elif shout[i+1]==1:
            stairs.append(shout[i])
    print(len(stairs))
    for ele in stairs[0:len(stairs)-1]:
        print(str(ele),end=" ")
    print(stairs[-1])

if __name__=='__main__':
    Tanya_climbStairs()