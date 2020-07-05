n=int(input())
times=1
if n<26:
    print(chr(64+n))
else:
    result=''
    num=n//26+(n%26!=0)
    result+=chr(63+num)
    result+=chr(64+n%26)
    print(result)
