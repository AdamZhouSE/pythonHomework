def Test():
    n=int(input())
    boys=eval("["+input().strip().replace(" ",",")+"]")
    m=int(input())
    girls=eval("["+input().strip().replace(" ",",")+"]")
    a=save(boys)
    b=save(girls)
    z=min(m,n)
    all=[]
    j=0
    for i in range(0,z):
        parts=[]
        if(z==n):
            while(j<len(girls)):
                if(check(boys[0],girls[j])):
                    parts.append([boys[0],girls[j]])
                    boys.remove(boys[0])
                    girls.remove(girls[j])
                    j=0
                else:
                    j=j+1
        else:
            while(j<len(boys)):
                if (check(girls[0], boys[j])):
                    parts.append([boys[j], girls[0]])
                    boys.remove(boys[j])
                    girls.remove(girls[0])
                    j=0
                else:
                    j=j+1
        boys=save(a)
        girls=save(b)
        all.append(len(parts))
    print(max(all))
    print(n)
    print(a)
    print(m)
    print(b)

def check(a,b):
    return abs(a-b)<=1
def save(x):
    q=[]
    for v in x:
        q.append(v)
    return q
if __name__ == "__main__":
    Test()