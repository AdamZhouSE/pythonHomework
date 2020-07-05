#线性表中最大的和
def max_sum(A,m1,B,m2):
    re=[]

    count=0
    m=0
    for i in range(0,len(A)-m1+1):
        for j in range(i,i+m1):
            count=count+int(A[j])
        if count>m:
            m=count
            count=0
        count=0
    re.append(m)
    count1 = 0
    l = 0
    for i in range(0, len(B) - m2 + 1):
        for j in range(i, i + m2):
            count1 = count1 + int(B[j])
        if count1 > l:
            l = count1
            count1 = 0
        count1 = 0
    re.append(l)
    return re

if __name__ == '__main__':
    o=input()
    p=input()
    m1=int(p.split(" ")[1])
    A1=input()
    q=input()
    m2=int(q.split(" ")[1])
    B1=input()
    A=A1.split(" ")
    B=B1.split(" ")
    re=max_sum(A,m1,B,m2)
    print(re[0])
    print(re[1])