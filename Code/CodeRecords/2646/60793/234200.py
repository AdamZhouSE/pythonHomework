totalInput = int(input())
inputs = []
for i in range(0, totalInput):
    inputs.append(int(input()))
for x in inputs:
    if x%2 != 0:
        print("Player A")
    else:
        print("Player B")