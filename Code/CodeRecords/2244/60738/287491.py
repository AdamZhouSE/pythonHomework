n=int(input())
def prime(num):
    for i in range(2,int(num/2)):
        if num%i==0:
            return False
    return True
def huiwen(num):
    string=str(num)
    list1=list(string)
    list2=list1.copy()
    list1.reverse()
    if (str(list1)==str(list2)):
        return True
for j in range(n,200000000):
    if(prime(j) and huiwen(j)):
        print(j)
        break
