str0=input()
l=len(str0)
def isT(num):
    while num>1:
        if num%2!=0:
            return False
        num//=2
    return True
for i in range(pow(10,l-1),pow(10,l)):
    isR=False
    if isT(i):
        list0=list(str0)
        list0.sort()
        str0=''.join(list0)
        list1 = list(str(i))
        list1.sort()
        str1 = ''.join(list1)
        if str1==str0:
            isR=True
            break
print(isR)