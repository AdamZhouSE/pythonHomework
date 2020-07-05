def dp(X:int,Y:int,depth:int,f:bool)->int:
    if X==Y:
        return depth
    elif X>Y:
        return (X-Y)+depth
    if Y%2==1:
        return dp(X,Y+1,depth+1,True)
    elif f:
        return dp(X,Y//2,depth+1,False)
    else:
        return min(dp(X,Y//2,depth+1,False),dp(X,Y+1,depth+1,True))

X=int(input())
Y=int(input())
print(dp(X,Y,0,False))
#欲抵达Y，须先抵达Y+1或Y//2
#乘2得不到奇数，所以Y为奇数时只能抵达Y+1
#不可能连续两次都抵达Y+1，因为此时等同于抵达Y+2，即（Y//2）+1，以f标记
#X比Y大时，只能通过Y+1抵达
#抵达Y时，X与Y相等