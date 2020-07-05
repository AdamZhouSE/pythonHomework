
def splitArraySameAverage( A):
    from fractions import Fraction    #!!!!!!!!
    N = len(A)
    S = sum(A)
    A = [z - Fraction(S, N) for z in A]   #z-平均数

    if N == 1: return False

    #Want zero subset sum
    left = {A[0]}
    for i in range(1, N//2):
        left = {z + A[i] for z in left} | left | {A[i]}   #!!!!!!!!!!
    if 0 in left: return True

    right = {A[-1]}
    for i in range(N//2, N-1):
        right = {z + A[i] for z in right} | right | {A[i]}
    if 0 in right: return True

    sleft = sum(A[i] for i in range(N//2))
    sright = sum(A[i] for i in range(N//2, N))

    return any(-ha in right and (ha, -ha) != (sleft, sright) for ha in left)
    #若ha==sleft, -ha==sright，那么说明所有元素都被选了，那么另一个数组就为空了
    #ha -ha 是由哪些元素出来，那么其中一个数组就由这些元素构成，剩下元素就构成另一个数组
if splitArraySameAverage(eval("["+input()+"]")): print("True")
else: print("False")

