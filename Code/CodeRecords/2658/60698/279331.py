def test():
    t = int(input())
    for _ in range(0, t):
        nx=input().split()
        n=int(nx[0])
        x=int(nx[1])
        arr=input().split()
        arr=list(map(int,arr))
        multiple=[]
        for i in range(0,len(arr)):
            if arr[i]%x==0 and arr[i] not in multiple:
                multiple.append(arr[i])
        if len(multiple)==0:
            print(0)
            return
        multiple.sort(reverse=True)
        bins=[]
        binary=bin(multiple[0])
        binary.replace("0b","")
        length=len(binary)
        bins.append(binary)
        for i in range(0,len(multiple)):
            binary=bin(multiple[i]).replace("0b","")
            if binary in bins:
                continue
            else:
                while length>len(binary):
                    binary='0'+binary
                bins.append(binary)
        res=['0']*length
        for binary in bins:
            for j in range(0,length):
                if str(binary)[j]=='1':
                    res[j]='1'
        res=''.join(res)
        res=int(res,2)
        print(res)
test()
