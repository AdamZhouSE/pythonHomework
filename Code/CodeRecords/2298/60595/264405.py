def Test():
    n=int(input())
    nums=eval("["+input().replace(" ",",")+"]")
    zu=[-1 for _ in range(0,10000)]
    for k in range(0,len(nums)):
        x=nums[k]
        if(k==0):
            zu[1]=x
            print(-1)
            continue
        else:
            i=1
            while(True):
                if(zu[i]>=x and zu[i]!=-1):
                    i=i*2
                    if(zu[i]==-1):
                        zu[i]=x
                        break
                elif(zu[i]<=x and zu[i]!=-1):
                    i=i*2+1
                    if(zu[i]==-1):
                        zu[i]=x
                        break
            print(findFather(zu,x))
def findFather(zu,x):
    i=zu.index(x)
    if (i % 2 == 0):
        i = i // 2
    else:
        i = (i - 1) // 2
    return zu[i]
if __name__ == "__main__":
    Test()