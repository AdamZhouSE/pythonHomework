#找出出现次数超过n/3的元素
def solve(A):
    B=[]
    for i in A:
        k=0
        k=A.count(i)
        if k>len(A)//3:
            B.append(i)
    C=list(set(B))
    return C


if __name__ == '__main__':
    A=eval(input())
    re=solve(A)
    print(re)