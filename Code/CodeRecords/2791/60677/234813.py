n=int(input())
voices=input().split()
voicestr=''.join(voices)
voices=voicestr.split('1')
voices.pop(0)
print(voices.__len__())
answer=[]
for i in voices:
    answer.append(i.__len__()+1)
answer=[str(x) for x in answer]
print(' '.join(answer))