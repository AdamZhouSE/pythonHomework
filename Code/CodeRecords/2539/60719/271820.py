new = input()
new = new[1:len(new)-1].split(",")
for i in range(len(new)):
    new[i] = int(new[i])
old = new.copy()
new.sort()
ol = []
nl = []
for x in new:
    ol.append(old.index(x))
    nl.append(new.index(x))
start = 0
end = 0
for i in range(len(ol)):
    if ol[i] != nl[i]:
        if start == 0 and ol[0] == nl[0]:
            start = i
        end = i
print(end-start+1)
