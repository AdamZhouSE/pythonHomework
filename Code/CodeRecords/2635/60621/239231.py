def count(n):
    res=0
    while n>0:
        res+=(n//5)
        n//=5
    return res>=K

K=int(input())
def find(K):
    large, small = 5 * K + 5, K
    while small<large:
        middle=(large+small)//2
        if(count(middle)):
            small=middle+1
        else:
            large=middle
    return large//5*5
print(find(K+1)-find(K))