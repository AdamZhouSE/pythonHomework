word1=input()
word2=input()
string1=[]
string2=[]
num=0
for i in range(len(word1)):
    for j in range(i+1,len(word1)+1):
        string1.append(word1[i:j])
for i in range(len(word2)):
    for j in range(i+1,len(word2)+1):
        string2.append(word2[i:j])
for i in range(len(string1)):
    for j in range(len(string2)):
        if string1[i]==string2[j]:
             num=num+1
print(num)