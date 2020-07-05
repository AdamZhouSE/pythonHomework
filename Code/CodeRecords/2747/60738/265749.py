String1=input()
String2=input()
word_list=eval(input())
all_list=[]
output=[]
length=len(word_list)
def nextWordList(word,word_list):
    temp_list=[]
    word_length=len(word)
    time=0
    for element in word_list:
        for i in range(word_length):
            if element[i]!=word[i]:
                time+=1
        if time==1:
            temp_list.append(element)
    return temp_list
stack=[beginWord]
while stack:
    temp_list=[]
    for j in nextWordList(stack[-1]):
        while j!=String2:
            
        
    


    

