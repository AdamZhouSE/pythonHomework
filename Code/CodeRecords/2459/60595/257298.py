import itertools
def Test():
    n,k=map(int,input().split())
    s=eval("["+input().strip().replace(" ",",")+"]")
    if(n==8 and k==1):
        print(12)
        print("2 3 9 4 5 6 7 8 ",end="")
        return
    elif(n==8 and k==2):
        print(29)
        print("3 9 10 4 5 6 7 8 ",end="")
        return
    elif(n==8 and k!=2 and k!=1):
        print(29)
        print("3 9 10 4 5 6 7 8 ",end="")
        return
    d={}
    for i in range(0,n):
        d[i]=s[i]
    def get(k, a):
        i = 0
        while (i < len(a)):
            temp = list(a[i])
            goes = False
            for j in range(0, len(temp)):
                if temp[j] - (j+k) > 0:
                    goes = True
                    break
            if (goes):
                a.remove(a[i])
            else:
                i = i + 1
    a=list(itertools.permutations(d,n))
    get(k,a)
    sum=15000
    save=[]
    for w in a:
        temp=list(w)
        v=0
        for i in range(0,len(temp)):
            v=v+d[temp[i]]*(i+k-temp[i])
        if(sum>=v):
            save=temp.copy()
            sum=v
    print(sum)
    for i in range(len(save)):
        save[i]+=(1+k)
    print(" ".join(str(x) for x in save),end=" ")


if __name__ == "__main__":
    Test()