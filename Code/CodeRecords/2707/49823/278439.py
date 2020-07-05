def ax(l):

    r=0
    for i in range(len(l)//2-1):
        a=l[2*i]
        b=l[2*i+1]
        if not ((a&1 and b==a-1) or (b&1 and a+1==b)):
            if a&1:
                for j in range(2*i+2,len(l)):
                    if l[j]==a-1:
                        l[2*i+1],l[j]=l[j],l[2*i+1]
                        r+=1
                        break
            else:
                for j in range(2*i+2,len(l)):
                    if l[j]==a+1:
                        l[2*i+1],l[j]=l[j],l[2*i+1]
                        r+=1
                        break
    print(r)

if __name__ == '__main__':
    ax(eval(input()))
