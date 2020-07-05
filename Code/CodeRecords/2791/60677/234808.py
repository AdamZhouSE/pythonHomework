n=int(input())
voices=input().split()
voicestr=''.join(voices)
voices=voicestr.split('1')
voices.pop(0)
print(voices.__len__())
for i in voices:
    print(i.__len__()+1,end=' ')