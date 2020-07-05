def Test():
    n=int(input())
    boys=eval("["+input().strip().replace(" ",",")+"]")
    m=int(input())
    girls=eval("["+input().strip().replace(" ",",")+"]")
    z=min(m,n)
    parts=[]
    j=0
    if(z==n):
        while(j<len(girls)):
            if(check(boys[0],girls[j])):
                parts.append([boys[0],girls[j]])
                boys.remove(boys[0])
                girls.remove(girls[j])
            else:
                j=j+1
    else:
        while(j<len(boys)):
            if (check(girls[0], boys[j])):
                parts.append([boys[j], girls[0]])
                boys.remove(boys[j])
                girls.remove(girls[0])
            else:
                j=j+1
    print(len(parts))

def check(a,b):
    return abs(a-b)<=1
if __name__ == "__main__":
    Test()