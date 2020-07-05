n = int(input())
list0 = [1,2,3,4,5,6,8]
count = 7
if n<=7 : print(list0[n-1])
else:
    for num in range(9,1000000):
        result = True
        transtwo = False
        transthree = False
        transfive = False
        trans = transtwo and transthree and transfive
        while trans:
            if num%2!=0:transtwo = True
            else: num //=2
            if num%3!=0:transthree = True
            else: num //=3
            if num%5!=0:transfive = True
            else: num //=5
            trans = transtwo and transthree and transfive
        for i in range(6,num+1):
            if num%i==0 and i%2!=0 and i%3!=0 and i%5!=0:
                result = False
                break
        if result :
            count +=1
            list0.append(num)
            if count == n:
                print(num)
                break
