def like(word1,word2):
    string1=''
    string2=''
    n=len(word1)
    m=len(word2)
    indicate=0
    if n!=m:
        return False
    for i in range(n):
        if word1[i]==word2[i]:
            continue
        else:
            string1+=word1[i]
            string2+=word2[i]
            indicate+=1
    if indicate>2:
        return False
    elif set(string1)==set(string2):
        return True

words=input()
num=0
for i in range(len(words)):
    for j in range(i,len(words)):
        if like(words[i],words[j]):
            num+=1
    num-=1

print(num)