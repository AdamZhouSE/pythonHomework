def connell(n):
    if n==1:
        return "1"
    else:
        even=[2*i for i in range(1,n)]
        odd=[2*i-1 for i in range(1,n)]
        res=[1]
        i=2
        while len(res)<n:
            begin=0
            if i%2==0:
                for item in even:
                    if item > res[-1]:
                        begin = even.index(item)
                        break
                slice = even[begin:begin + i]
                res = res + slice
                even = even[i+begin:]
                i += 1
            else:
                for item in odd:
                    if item > res[-1]:
                        begin = odd.index(item)
                        break
                slice = odd[begin:begin + i]
                res = res + slice
                odd = odd[i+begin:]
                i += 1
        res=res[:n]
        res=[str(x) for x in res]
        return " ".join(res)

if __name__=="__main__":
    tests=int(input())
    cnt=0
    while cnt<tests:
        n=int(input())
        ans=connell(n)
        print(ans)
        cnt+=1