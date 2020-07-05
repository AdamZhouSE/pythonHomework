class Node:
    def __init__(self,value):
        self.value=value
        self.children=[]
        self.clock=-1

    def next_node(self):
        self.clock=self.clock+1
        if self.clock>len(self.children)-1:
            return None
        return self.children[self.clock]

def compare_word(wordA,wordB):
    count=0
    for i in range(len(wordA)):
        if wordA[i]!=wordB[i]:
            count=count+1
    return count==1

beginWord=input()
endWord=input()
wordList=list(eval(input()))
wordList.insert(0,beginWord)
word=[]
for i in range(len(wordList)):
    current=Node(value=wordList[i])
    word.append(current)
for i in range(len(wordList)-1):
    current=word[i]
    for j in range(len(wordList)-1,i,-1):
        if compare_word(wordList[i],wordList[j]):
            current.children.append(word[j])
current=word[0]
stack=[current]
ans=[]
while len(stack)!=0:
    current=current.next_node()
    while current is not None:
        stack.append(current)
        current=current.next_node()
    res=[]
    for i in range(len(stack)):
        res.append(stack[i].value)
    if stack[len(stack)-1].value==endWord:
        ans.append(res)
    stack.pop()#最后一个，且没有向下节点了
    if len(stack)!=0:
        current=stack[len(stack)-1]#倒数第二个，有可能有向下节点
ans.sort(key=len)
if len(ans)==0:
    print([])
else:
    min_length=len(ans[0])
    res=[]
    for i in ans:
        if len(i)==min_length:
            res.append(i)
        else:
            break
    print(res)