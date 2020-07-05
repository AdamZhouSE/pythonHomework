line = input();
#print(line);
n = len(line);
s = [];
for i in range(n):
    s.append(line[i]);
line= input();
#print(line)
a = line[0];

string = '';
if a == 'D':
    b = line[3]
    t = 0;
    for i in range(n):
        if s[i] == b:
            break;
        t += 1;
    for i in range(t+1, n):
        s[i-1] = s[i];
    n -=1;
    for i in range(n):
        string += s[i]
if a == 'I':
    b  = line[3];
    c = line[5]; #存疑
    s.append('');
    for i in range(n):
        if s[i] == b:
            t = i;
    for i in range(n-1, t-1, -1):
        s[i+1] = s[i];
    s[t] = c;
    for i in range(n+1):
        string += s[i]
if a == 'R':
    b  = line[3];
    c = line[5]; #存疑
    t = 0;
    for i in range(n):
        if s[i] == b:
            s[i] = c;
    for i in range(n):
        string += s[i]
print(string);