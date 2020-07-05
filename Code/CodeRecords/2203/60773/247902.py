s=input()
for i in range(len(s)):
    if i==0 or i==1:
        print(0)
    else:
        sum=0
        for m in range(0,i-1,1):
            for n in range(m+1,i,1):
                # print("m",end="")
                # print(m)
                # print("n", end="")
                # print(n)
                if s[m]==s[n]:
                    # print("i+2-n", end="")
                    # print(i+2-n)
                    count = 1
                    for k in range(1,i+2-n,1):
                        if m+k<=i and n+k<=i:
                            if s[m+k]==s[n+k]:
                                count=count+1
                                # print("count", end="")
                                # print(count)
                                if(count>n-m):sum=sum+count
                            else:
                                break


        print(sum)