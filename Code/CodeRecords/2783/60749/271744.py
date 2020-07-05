n=int(input())
dictionary={}
ans=[]
for _ in range(n):
    ans.append(input().split(" "))
for h in ans:
    if h[0] in dictionary.keys():
        dictionary[h[0]]+=int(h[1])
    else:
        dictionary[h[0]]=int(h[1])

temp=[]
for k in dictionary.keys():
    temp.append(dictionary[k])
maxvalue=sorted(temp)[-1]
def output_name(ans,dictionary,maxvalue):
    for h in ans:
        if h[0] in dictionary:
            dictionary[h[0]] += int(h[1])
            if dictionary[h[0]]==maxvalue:
                return h[0]
        else:
            dictionary[h[0]] = int(h[1])
            if dictionary[h[0]]==maxvalue:
                return h[0]
dictionary2={}
print(output_name(ans,dictionary2,maxvalue))