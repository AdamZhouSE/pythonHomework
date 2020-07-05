def add(index:str):
    a = adder.split('/')
    b = index.split('/')
    a1 = int(a[0])
    a2 = int(a[1])
    b1 = int(b[0])
    b2 = int(b[1])
    ma = a2*b2
    chi1 = a1*b2
    chi2 = b1*a2
    child = chi1 + chi2
    ans = "{}/{}".format(child,ma)
    return ans

def gcd(a,b):
    if a%b == 0:
        return b
    else :
        return gcd(b,a%b)

def toSimple(string:str):
    a = string.split('/')
    a1 = int(a[0])
    a2 = int(a[1])
    while True:
        k = gcd(abs(a1),abs(a2))
        if k==1:
            break;
        else:
            a1 = a1//k
            a2 = a2//k
    ans = "{}/{}".format(a1,a2)
    return ans

strs = input()
lists = list()
temp = 0
for i in range(len(strs)):
    if strs[i]=='+' or strs[i]=='-' or i==0:
        for j in range(i+1,len(strs)):
            if strs[j]=='+' or strs[j]=='-':
                lists.append(strs[i:j])
                i = j
                break
            if j == len(strs)-1:
                lists.append(strs[i:j+1])
                break
adder = "0/1"
for i in range(len(lists)):
    adder = add(lists[i])
adder = toSimple(adder)
print(adder)
