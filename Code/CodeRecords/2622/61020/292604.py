str_input = input().split(',')
recorder = {}
for c in str_input:
    if c in recorder:
        recorder[c] += 1
    else:
        recorder[c] = 1

print(max(list(recorder.keys()), key=lambda x: recorder[x]))
