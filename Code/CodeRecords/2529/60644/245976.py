def f(lst,arr,dex):
    if dex==1:

        num=int("".join(lst))
        while num!=1:


            if num%2==1:
                return
            else:
                num=num/2

        return True
    else:
        for i in range(0,dex):

            temp=lst[dex-1]
            lst[dex-1]=lst[i]
            lst[i]=temp
            if   f(lst,arr,dex-1):
                return True



            temp = lst[dex - 1]
            lst[dex - 1] = lst[i]
            lst[i] = temp






num=input()
lst=list(num)
arr=[]
res=[]
if num.count('0')>0:
    print('false')
else:
    num = int(num)
    if num == 1:
        print('true')
    else:
        if f(lst, arr, len(lst)):
            print('true')
        else:
            print('false')


