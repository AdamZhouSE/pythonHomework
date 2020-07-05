import collections
s=input()
maxLetters=int(input())
minSize=int(input())
maxSize=int(input())
result=next((i for x,i in collections.Counter(s[i-minSize:i] for i in range(minSize,len(s)+1)).most_common() if len(set(x))<=maxLetters),0)
print(result)