def Test():
    s=input().split()
    a=bin(int(s[0]))[2:]
    b=bin(int(s[1]))[2:]
    while(len(a)!=len(b)):
        if(len(a)>len(b)):
            b="0"+b
        else:
            a="0"+a
    print(check(a,b))

def check(a,b):
    i=-1
    while(i>=-len(a)):
        if(a[i]!=b[i]):
            return -i
        i=i-1
    return -1

if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()