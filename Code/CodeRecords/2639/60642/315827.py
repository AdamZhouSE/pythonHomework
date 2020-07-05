def finder(string,k):
    out = 0
    for i in string:
        if(i==string[0]):
            out+=1
        elif(k>0):
            k-=1
            out+=1
        else:
            break
    return out

string = input()
k = int(input())
chars = []
for i in string:
    if(chars.count(i)==0):
        chars.append(i)
out = 0
for i in chars:
    for j in range(len(string)):
        if(string[j]==i):
            temp = finder(string[j:], k)
            out = max(temp,out)
print(out)