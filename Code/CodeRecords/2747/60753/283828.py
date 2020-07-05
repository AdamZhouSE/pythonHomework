import sys
import Queue
s=sys.stdin.read()
sli=s.split("\n")
beginword=sli[0]
endword=sli[1]
wordlist1=sli[2].split(",")
wordlist=[]
for word in wordlist1:
    wordli=list(word)
    standard=""
    for ch in wordli:
        if ch!="[" and ch!='"' and ch!="]":
            standard+=ch
    wordlist.append(standard)
ans=[]
queue=Queue.Queue()
dic={}
solution=[]
for s in wordlist:
    dic[s]=1
queue.put(beginword)
queue.put(",")
while not queue.empty():
    wordstr=queue.get()
    solution.append(wordstr)
    words=list(wordstr)
    if wordstr !=",":
        for i in range(len(words)):
            tmp=words[i]
            alphabet="abcdefghijklmnopqrstuvwxyz"
            for j in alphabet:
                if j==words[i]:
                    continue
                words[i]=j
                wordrevise="".join(words)
                for key in dic:
                    if key==wordrevise and dic[key]!=0:
                        queue.put(wordrevise)
                        dic[wordrevise]=0
                        if wordrevise==endword:
                            ans.append(solution)
            words[i]=tmp 
    elif not queue.empty:
        queue.put(",")
print(ans)
                            
                    
                
                

