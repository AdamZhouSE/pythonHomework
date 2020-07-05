t = input()
times = []
appeared = []
for chara in t:
    if chara in appeared:
        times[appeared.index(chara)] += 1
    else:
        times.append(1)
        appeared.append(chara)
if len(times) > 1:
    k = len(times) - 1
    while k > 0:
        for i in range(k):
            if times[i] > times[i+1]:
                temp1 = times[i+1]
                times[i+1] = times[i]
                times[i] = temp1
                temp2 = appeared[i+1]
                appeared[i+1] = appeared[i]
                appeared[i] = temp2
        k -= 1
result = ""
end = len(times) - 1
while end >= 0:
    result += appeared[end] * times[end]
    end -= 1
print(result)