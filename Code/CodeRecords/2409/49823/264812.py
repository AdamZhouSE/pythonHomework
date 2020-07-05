def ae(l):
    r=len(l)*2
    for i in range(len(l)):
        temp=0
        for j in range(len(l)):
            temp+=int((l[j]-l[i])%2==1)
        r=min(r,temp)
    print(r)

if __name__ == '__main__':
    ae([int(i) for i in input().split(',')])
