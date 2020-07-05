def func(A,B,C,D):
    sum2=dict()
    ret=0
    for a in A:
        for b in B:
            s=a+b
            if s not in sum2:
                sum2[s]=1
            else:
                sum2[s]+=1
    for c in C:
        for d in D:
            k=c+d
            if -k in sum2: ret+=sum2[-k]
    return ret
A=eval("["+input()+"]")
B=eval("["+input()+"]")
C=eval("["+input()+"]")
D=eval("["+input()+"]")
print(func(A,B,C,D))