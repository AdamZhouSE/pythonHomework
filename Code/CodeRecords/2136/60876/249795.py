num=int(input())
def good(k):
    jud=True
    n=num
    while n!=1:
        if n%k!=1:
            jud=False
            break
        n=n//k
    return jud
temp=2
while not good(temp):
    temp+=1
print(temp)