t = int(input())
for i in range(t):
    raw = input()
    new = raw.replace("6","9")
    print(int(new)-int(raw))