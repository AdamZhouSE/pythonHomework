final_len,limit=map(int,input().split())
text=input()
count=int(input())
for i in range(0,count):
    a,b,c=map(int,input().split());
    current=text[a:b]
    text=text[0:c]+current+text[c:]
    if(len(text)>limit):
        text=text[0:limit]
print(text[0:final_len],end="")