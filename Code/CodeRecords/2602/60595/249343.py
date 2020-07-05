def Test(A,B):
    if(len(A)<1 or len(B)<1):
        return ""
    if (A.count(B)!=0):
        return B
    elif(len(B)!=0):
        return ""
    left=Test(A,B[:len(B)-1])
    right=Test(A,B[1:])
    return left if(len(left)>=len(right)) else right

if __name__ == "__main__":
    A="".join(str(x) for x in eval(input()))
    B="".join(str(x) for x in eval(input()))
    print(len(Test(A,B)))