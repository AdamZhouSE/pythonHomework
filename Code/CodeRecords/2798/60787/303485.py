n=int(input())
num=[int(i) for i in input().split()]
if not sum(num)%3==0:
    print(0)
else:
    s=int(sum(num)/3)
    flag=True
    temp,cut1,cut2=0,-1,-1
    if not s==0:
        for i in range(0,n):
            temp+=num[i]
            if temp==s:
                temp=0
                if cut1==-1:
                    cut1=i
                elif cut2==-1:
                    cut2=i
            elif temp>s:
                print(0)
                flag=False
                break
        if flag:
            zero1,zero2=0,0
            if num[cut1+1]==0:
                for i in range(cut1+1,cut2):
                    if num[i]==0:
                        zero1+=1
                    else:
                        break
            if num[cut2+1]==0:
                for i in range(cut2+1,n):
                    if num[i]==0:
                        zero2+=1
                    else:
                        break
            if zero1==0 and zero2==0:
                print(1)
            elif zero1==0:
                print(zero2+1)
            elif zero2==0:
                print(zero1+1)
            else:
                print((zero1+1)*(zero2+1))
        else:
            print(3)