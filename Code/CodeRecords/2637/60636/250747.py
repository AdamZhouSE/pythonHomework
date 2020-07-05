sources=eval(input())
for i in range(len(sources)):
    if sources[i]>sources[i-1] and sources[i]>sources[i+1]:
        print(i)
        break