n=int(input())
voices=input().split()
voicestr=''.join(voices)
voices=voicestr.split('1')
voices.pop(0)
print(voices.__len__())
for i in voices:
    if i!=voices.__len__()-1:
        print(i.__len__()+1,end=' ')
    else:
        print(i.__len__()+1)